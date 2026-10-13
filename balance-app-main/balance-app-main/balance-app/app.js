// State Management
let expenses = JSON.parse(localStorage.getItem('balance_expenses')) || [];
let incomes = JSON.parse(localStorage.getItem('balance_incomes')) || [];
let currentDate = new Date(); // Start with current actual date
let expensesChartInstance = null; // Holds the Chart.js instance for dashboard
let compareChartInstance = null; // Holds the Chart.js instance for compare view
let simulatorChartInstance = null; // Holds the Chart.js instance for simulator
let chartStartIndex = null; // Starting index for the 12-month window in the compare chart
let selectedCompareMonths = new Set();
let selectedWorkshopMonths = new Set();
let projects = JSON.parse(localStorage.getItem('balance_projects')) || [];

// Migration for legacy project costs -> extraExpenses
projects.forEach(project => {
    if (!project.extraExpenses) project.extraExpenses = [];
    let migrated = false;
    if (parseFloat(project.costMaterials) > 0) {
        project.extraExpenses.push({ desc: 'Costo Materiales', amount: parseFloat(project.costMaterials), date: project.startDate });
        project.costMaterials = 0;
        migrated = true;
    }
    if (parseFloat(project.costLabor) > 0) {
        project.extraExpenses.push({ desc: 'Costo Elaboración', amount: parseFloat(project.costLabor), date: project.startDate });
        project.costLabor = 0;
        migrated = true;
    }
    const hours = parseFloat(project.hours) || 0;
    const rate = parseFloat(project.hourlyRate) || 0;
    if (hours > 0 && rate > 0) {
        project.extraExpenses.push({ desc: `Horas de Trabajo (${hours}h)`, amount: hours * rate, date: project.startDate });
        project.hours = 0;
        project.hourlyRate = 0;
        migrated = true;
    }
    
    // Migrate expectedIncome to expectedIncomes array
    if (!project.expectedIncomes) {
        project.expectedIncomes = [];
        const expInc = parseFloat(project.expectedIncome) || 0;
        const expMos = parseInt(project.expectedMonths) || 1;
        if (expInc > 0) {
            project.expectedIncomes.push({ desc: `Ingreso Estimado (${expMos} meses)`, amount: expInc * expMos, date: project.startDate });
            project.expectedIncome = 0;
            migrated = true;
        }
    }
    
    // Reparación de fechas guardadas erróneamente como DD/MM/YYYY
    if (project.extraExpenses) {
        project.extraExpenses.forEach(exp => {
            if (exp.date && exp.date.includes('/')) {
                const parts = exp.date.split('/');
                if (parts.length === 3) {
                    exp.date = `${parts[2]}-${parts[1].padStart(2, '0')}-${parts[0].padStart(2, '0')}`;
                    migrated = true;
                }
            }
        });
    }
    if (project.expectedIncomes) {
        project.expectedIncomes.forEach(inc => {
            if (inc.date && inc.date.includes('/')) {
                const parts = inc.date.split('/');
                if (parts.length === 3) {
                    inc.date = `${parts[2]}-${parts[1].padStart(2, '0')}-${parts[0].padStart(2, '0')}`;
                    migrated = true;
                }
            }
        });
    }
});
localStorage.setItem('balance_projects', JSON.stringify(projects));

let activeProjectId = null; // For the detail view
let draggedProjectId = null; // For drag and drop reordering
let returnToProjectId = null; // Return to project modal after adding expense/income
let simulatedProjects = []; // Array para múltiples proyectos en el simulador
let workshopConfig = JSON.parse(localStorage.getItem('balance_workshop_config')) || { name: 'Horario Habitual', startTime: '09:00', endTime: '18:00', isActive: true };
let users = JSON.parse(localStorage.getItem('balance_users')) || [
    { id: 'u_1', name: 'Raúl', aliases: ['M CIRIGLIANO GEREZ', 'Raúl'] },
    { id: 'u_2', name: 'Milagros', aliases: ['R CIRIGLIANO COYTO', 'Milagros'] }
];
let cardsConfig = JSON.parse(localStorage.getItem('balance_cards')) || [
    { id: 'c_visa', name: 'Visa', type: 'visa', aliases: ['Visa'] },
    { id: 'c_master', name: 'Mastercard', type: 'master', aliases: ['Mastercard'] },
    { id: 'c_mp', name: 'Mercado Pago', type: 'mercado', aliases: ['Mercado Pago', 'MercadoPago'] },
    { id: 'c_efec', name: 'Efectivo / Débito', type: 'efectivo', aliases: ['Efectivo', 'Debito', 'Efectivo/Debito'] },
    { id: 'c_tax', name: 'Impuestos y Servicios', type: 'impuestos', aliases: ['Impuestos', 'Servicios'] }
];
let usdRateConfig = JSON.parse(localStorage.getItem('balance_usd_rate')) || 1000;

const getCardTypeByName = (cardName) => {
    const c = cardsConfig.find(c => c.name === cardName);
    if (c) return c.type;
    
    const lower = (cardName || '').toLowerCase();
    if (lower.includes('visa')) return 'visa';
    if (lower.includes('master')) return 'master';
    if (lower.includes('mercado')) return 'mercado';
    if (lower.includes('impuesto') || lower.includes('servicios')) return 'impuestos';
    return 'efectivo';
};

// Chart.js Plugins
if (typeof ChartDataLabels !== 'undefined') {
    Chart.register(ChartDataLabels);
}

// DOM Elements
const btnAddExpense = document.getElementById('btn-add-expense');
const modalOverlay = document.getElementById('add-expense-modal');
const btnCloseModal = document.getElementById('close-modal');
const btnCancel = document.getElementById('btn-cancel');
const expenseForm = document.getElementById('expense-form');
const expenseIsUsd = document.getElementById('expense-is-usd');

const currentMonthDisplay = document.getElementById('current-month-display');
const btnPrevMonth = document.getElementById('prev-month');
const btnNextMonth = document.getElementById('next-month');

// Summary Cards
const totalIncomes = document.getElementById('total-incomes');
const totalExpenses = document.getElementById('total-expenses');
const totalBalance = document.getElementById('total-balance');
const balanceCard = document.getElementById('balance-card');
const expenseList = document.getElementById('expense-list');
const emptyState = document.getElementById('empty-state');
const expenseTable = document.getElementById('expense-table');
const tableFooterTotal = document.getElementById('table-footer-total');
const expenseTableFooter = document.getElementById('expense-table-footer');

// Incomes DOM
const btnAddIncome = document.getElementById('btn-add-income');
const incomeModalOverlay = document.getElementById('add-income-modal');
const btnCloseIncomeModal = document.getElementById('close-income-modal');
const btnCancelIncome = document.getElementById('btn-cancel-income');
const incomeForm = document.getElementById('income-form');
const incomeList = document.getElementById('income-list');
const incomeTable = document.getElementById('income-table');
const incomeSource = document.getElementById('income-source');
const incomeProjectContainer = document.getElementById('income-project-container');
const incomeProject = document.getElementById('income-project');
const incomeDate = document.getElementById('income-date');

// Filters
const filterTitular = document.getElementById('filter-titular');
const filterCard = document.getElementById('filter-card');
const filterType = document.getElementById('filter-type');
const filterIncomeType = document.getElementById('filter-income-type');

// User Management DOM
const usersListContainer = document.getElementById('users-list-container');
const newUserName = document.getElementById('new-user-name');
const btnAddUser = document.getElementById('btn-add-user');
const incomeTitular = document.getElementById('income-titular');
const expenseTitular = document.getElementById('expense-titular');

// Cards Management DOM
const cardsListContainer = document.getElementById('cards-list-container');
const newCardName = document.getElementById('new-card-name');
const newCardType = document.getElementById('new-card-type');
const btnAddCard = document.getElementById('btn-add-card');
const expenseCard = document.getElementById('expense-card');

// Navigation & Views
const navDashboard = document.getElementById('nav-dashboard');
const navCompare = document.getElementById('nav-compare');
const navHistory = document.getElementById('nav-history');
const navArchive = document.getElementById('nav-archive');
const navStats = document.getElementById('nav-stats');
const navSettings = document.getElementById('nav-settings');
const navHelp = document.getElementById('nav-help');
const viewDashboard = document.getElementById('view-dashboard');
const viewCompare = document.getElementById('view-compare');
const viewHistory = document.getElementById('view-history');
const viewWorkshop = document.getElementById('view-workshop');
const viewArchive = document.getElementById('view-archive');
const viewStats = document.getElementById('view-stats');
const viewSettings = document.getElementById('view-settings');
const viewHelp = document.getElementById('view-help');

const navWorkshop = document.getElementById('nav-workshop');
const projectsGrid = document.getElementById('projects-grid');
const archiveGrid = document.getElementById('archive-grid');
const workshopEmptyState = document.getElementById('workshop-empty-state');
const archiveEmptyState = document.getElementById('archive-empty-state');
const btnAddProject = document.getElementById('btn-add-project');
const projectModalOverlay = document.getElementById('add-project-modal');
const btnCloseProjectModal = document.getElementById('close-project-modal');
const workshopBalancesContainer = document.getElementById('workshop-balances-container');
const workshopSelectedSum = document.getElementById('workshop-selected-sum');
const btnWorkshopSelectAll = document.getElementById('btn-workshop-select-all');
const btnWorkshopClearAll = document.getElementById('btn-workshop-clear-all');
const btnRefreshWorkshopCalculator = document.getElementById('btn-refresh-workshop-calculator');
const workshopBalanceCalculator = document.getElementById('workshop-balance-calculator');
const btnCancelProject = document.getElementById('btn-cancel-project');
const projectForm = document.getElementById('project-form');
const btnAddProcessStep = document.getElementById('btn-add-process-step');
const projectProcessesList = document.getElementById('project-processes-list');

// Project Detail
const projectDetailModal = document.getElementById('project-detail-modal');
const btnCloseDetailModal = document.getElementById('close-detail-modal');
const detailProjectName = document.getElementById('detail-project-name');
const detailProjectDescription = document.getElementById('detail-project-description');
const detailProjectImg = document.getElementById('detail-project-img');
const detailProjectStatus = document.getElementById('detail-project-status');
const detailProjectDates = document.getElementById('detail-project-dates');
const detailProcessesList = document.getElementById('detail-processes-list');
const detailSchedulesList = document.getElementById('detail-schedules-list');
const btnAddSchedule = document.getElementById('btn-add-schedule');
const btnAddMonthlySchedule = document.getElementById('btn-add-monthly-schedule');
const btnExportGCal = document.getElementById('btn-export-gcal');
const btnSimulateProject = document.getElementById('btn-simulate-project');
const btnArchiveProject = document.getElementById('btn-archive-project');
const btnDeleteProject = document.getElementById('btn-delete-project');

// Schedule Modal
const addScheduleModal = document.getElementById('add-schedule-modal');
const btnCloseScheduleModal = document.getElementById('close-schedule-modal');
const btnCancelSchedule = document.getElementById('btn-cancel-schedule');
const scheduleForm = document.getElementById('schedule-form');
const historyList = document.getElementById('history-list');
const historyEmptyState = document.getElementById('history-empty-state');
const historyTable = document.getElementById('history-table');
const btnClearData = document.getElementById('btn-clear-data');
const btnExportBackup = document.getElementById('btn-export-backup');
const navCash = document.getElementById('nav-cash');
const viewCash = document.getElementById('view-cash');
const cashTheoreticalBalance = document.getElementById('cash-theoretical-balance');
const cashRealInput = document.getElementById('cash-real-input');
const cashDiffContainer = document.getElementById('cash-diff-container');
const cashDifferenceAmount = document.getElementById('cash-difference-amount');
const btnApplyCashAdjustment = document.getElementById('btn-apply-cash-adjustment');
const btnClearCash = document.getElementById('btn-clear-cash');
const btnClearCards = document.getElementById('btn-clear-cards');
const btnClearCashExpenses = document.getElementById('btn-clear-cash-expenses');
const btnClearIncomes = document.getElementById('btn-clear-incomes');
const btnClearProjects = document.getElementById('btn-clear-projects');
const btnClearAll = document.getElementById('btn-clear-all');
const btnExportCards = document.getElementById('btn-export-cards');
const btnExportCash = document.getElementById('btn-export-cash');
const btnImportPdf = document.getElementById('btn-import-pdf');
const importPdfFile = document.getElementById('import-pdf-file');
const btnImportBackupCards = document.getElementById('btn-import-backup-cards');
const btnImportBackupCash = document.getElementById('btn-import-backup-cash');
const btnImportFullBackup = document.getElementById('btn-import-full-backup');
const importBackupFile = document.getElementById('import-backup-file');
const btnExportProjects = document.getElementById('btn-export-projects');
const btnImportProjects = document.getElementById('btn-import-projects');
const importProjectsFile = document.getElementById('import-projects-file');

const usdExchangeRate = document.getElementById('usd-exchange-rate');
if (usdExchangeRate) {
    usdExchangeRate.value = usdRateConfig;
    usdExchangeRate.addEventListener('input', (e) => {
        usdRateConfig = parseFloat(e.target.value) || 1000;
        localStorage.setItem('balance_usd_rate', JSON.stringify(usdRateConfig));
    });
}

// Compare View Elements
const compareMaxMonth = document.getElementById('compare-max-month');
const compareMaxAmount = document.getElementById('compare-max-amount');
const compareTrendPast = document.getElementById('compare-trend-past');
const compareTrendPastDesc = document.getElementById('compare-trend-past-desc');
const compareTrendFuture = document.getElementById('compare-trend-future');
const compareTrendFutureDesc = document.getElementById('compare-trend-future-desc');
const btnChartPrev = document.getElementById('chart-prev');
const btnChartNext = document.getElementById('chart-next');
const compareMonthDisplay = document.getElementById('compare-month-display');
const btnComparePrev = document.getElementById('compare-prev-month');
const btnCompareNext = document.getElementById('compare-next-month');

const compareBalancesContainer = document.getElementById('compare-balances-container');
const compareSelectedSum = document.getElementById('compare-selected-sum');
const btnCompareSelectAll = document.getElementById('btn-compare-select-all');
const btnCompareClearAll = document.getElementById('btn-compare-clear-all');

// Stats Elements
const statsProjectList = document.getElementById('stats-project-list');
const statsOptgroupActive = document.getElementById('stats-optgroup-active');
const statsOptgroupArchived = document.getElementById('stats-optgroup-archived');
const statsTotalIncomes = document.getElementById('stats-total-incomes');
const statsTotalExpenses = document.getElementById('stats-total-expenses');
const statsTotalBalance = document.getElementById('stats-total-balance');
const statsBalanceCard = document.getElementById('stats-balance-card');
const statsIncomesList = document.getElementById('stats-incomes-list');
const statsExpensesList = document.getElementById('stats-expenses-list');
const statsMonthList = document.getElementById('stats-month-list');
const statsMonthsContainer = document.getElementById('stats-months-container');

// Simulator Elements
const simProjectSelect = document.getElementById('sim-project-select');
const simNameInput = document.getElementById('sim-name');
const simExpenseInput = document.getElementById('sim-expense');
const simInstallmentsInput = document.getElementById('sim-installments');
const simExpenseStartInput = document.getElementById('sim-expense-start');
const simIncomeInput = document.getElementById('sim-income');
const simIncomeStartInput = document.getElementById('sim-income-start');
const simProjectMonthsInput = document.getElementById('sim-project-months');
const simMonthsInput = document.getElementById('sim-months');
const btnAddSimProject = document.getElementById('btn-add-sim-project');
const simProjectsList = document.getElementById('sim-projects-list');
const btnSimulate = document.getElementById('btn-simulate');
const btnClearSim = document.getElementById('btn-clear-sim');
const simResults = document.getElementById('sim-results');
const btnSaveSimProject = document.getElementById('btn-save-sim-project');
const saveSimModal = document.getElementById('save-sim-modal');
const closeSaveSimModal = document.getElementById('close-save-sim-modal');
const btnCancelSaveSim = document.getElementById('btn-cancel-save-sim');
const saveSimForm = document.getElementById('save-sim-form');
const simProjectTitle = document.getElementById('sim-project-title');

// Workshop Status Card (Dashboard)
const workshopStatusCard = document.getElementById('workshop-status-card');
const workshopStatusLabel = document.getElementById('workshop-status-label');
const workshopStatusTime = document.getElementById('workshop-status-time');
const workshopStatusIcon = document.getElementById('workshop-status-icon');

// Workshop Widget (Workshop View)
const workshopStatusWidget = document.getElementById('workshop-status-widget');
const workshopWidgetLabel = document.getElementById('workshop-widget-label');
const workshopWidgetTime = document.getElementById('workshop-widget-time');
const workshopWidgetIcon = document.getElementById('workshop-widget-icon');

// Workshop Config Modal
const editWorkshopModal = document.getElementById('edit-workshop-modal');
const closeWorkshopModal = document.getElementById('close-workshop-modal');
const workshopConfigForm = document.getElementById('workshop-config-form');
const workshopNameInput = document.getElementById('workshop-name');
const workshopIsActiveSelect = document.getElementById('workshop-is-active');
const workshopStartInput = document.getElementById('workshop-start');
const workshopEndInput = document.getElementById('workshop-end');
const btnCancelWorkshopConfig = document.getElementById('btn-cancel-workshop-config');

const scheduleNameInput = document.getElementById('schedule-name');

const btnEditProject = document.getElementById('btn-edit-project');
const projectModalTitle = document.getElementById('project-modal-title');
const projectDeadlineAlarm = document.getElementById('project-deadline-alarm');
const alarmText = document.getElementById('alarm-text');
const detailHistoryLog = document.getElementById('detail-history-log');

// Extra Expenses
const extraExpenseDesc = document.getElementById('extra-expense-desc');
const extraExpenseAmount = document.getElementById('extra-expense-amount');
const btnAddExtraExpense = document.getElementById('btn-add-extra-expense');
const extraExpensesList = document.getElementById('extra-expenses-list');

// Expected Incomes
const expectedIncomeDesc = document.getElementById('expected-income-desc');
const expectedIncomeAmount = document.getElementById('expected-income-amount');
const expectedIncomeQty = document.getElementById('expected-income-qty');
const btnAddExpectedIncome = document.getElementById('btn-add-expected-income');
const expectedIncomesList = document.getElementById('expected-incomes-list');

// Photo Gallery
const newPhotoUrl = document.getElementById('new-photo-url');
const btnAddPhoto = document.getElementById('btn-add-photo');
const projectPhotoGallery = document.getElementById('project-photo-gallery');
const photoFileInput = document.getElementById('photo-file-input');
const btnTriggerUpload = document.getElementById('btn-trigger-upload');
const projectImageFile = document.getElementById('project-image-file');
const btnUploadProjectImage = document.getElementById('btn-upload-project-image');

// Archive Income
const archiveIncomeModal = document.getElementById('archive-income-modal');
const archiveIncomeEndMonth = document.getElementById('archive-income-end-month');
let activeArchiveIncomeId = null;

// Formatters
const formatCurrency = (amount) => {
    return new Intl.NumberFormat('es-AR', {
        style: 'currency',
        currency: 'ARS'
    }).format(amount);
};

const formatDateDisplay = (dateStr) => {
    const options = { day: '2-digit', month: 'short', year: 'numeric' };
    return new Date(dateStr + 'T00:00:00').toLocaleDateString('es-AR', options);
};

// Utilities
const getMonthKey = (dateObj) => {
    return `${dateObj.getFullYear()}-${String(dateObj.getMonth() + 1).padStart(2, '0')}`;
};

const getMonthName = (dateObj) => {
    const month = dateObj.toLocaleDateString('es-AR', { month: 'long' });
    const year = dateObj.getFullYear();
    return `${month.charAt(0).toUpperCase() + month.slice(1)} ${year}`;
};

// Users Functions
const saveUsers = () => {
    localStorage.setItem('balance_users', JSON.stringify(users));
    populateTitularSelects();
    renderUsersSettings();
    renderApp();
};

const populateTitularSelects = () => {
    if (filterTitular) {
        const currentFilter = filterTitular.value;
        filterTitular.innerHTML = '<option value="all">Todos los Titulares</option>';
        users.forEach(u => {
            const opt = document.createElement('option');
            opt.value = u.name;
            opt.textContent = `Solo ${u.name}`;
            filterTitular.appendChild(opt);
        });
        if (Array.from(filterTitular.options).some(o => o.value === currentFilter)) {
            filterTitular.value = currentFilter;
        }
    }
    
    if (expenseTitular) {
        expenseTitular.innerHTML = '';
        users.forEach(u => {
            const opt = document.createElement('option');
            opt.value = u.name;
            opt.textContent = u.name;
            expenseTitular.appendChild(opt);
        });
    }

    if (incomeTitular) {
        incomeTitular.innerHTML = '';
        users.forEach(u => {
            const opt = document.createElement('option');
            opt.value = u.name;
            opt.textContent = u.name;
            incomeTitular.appendChild(opt);
        });
    }
};

const renderUsersSettings = () => {
    if (!usersListContainer) return;
    usersListContainer.innerHTML = '';
    users.forEach((u) => {
        const div = document.createElement('div');
        div.className = 'glassmorphism';
        div.style.padding = '1.2rem';
        div.style.background = 'rgba(255,255,255,0.05)';
        div.style.border = '1px solid var(--glass-border)';
        div.style.borderRadius = '8px';
        div.style.display = 'flex';
        div.style.flexDirection = 'column';
        
        const aliasesList = u.aliases.join(', ') || 'Sin alias';
        
        div.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
                <strong style="font-size: 1.1rem; color: var(--accent-primary);">${u.name}</strong>
                <button class="btn-icon" onclick="deleteUser('${u.id}')" style="color: var(--danger);" title="Eliminar Usuario"><i class="fa-solid fa-trash"></i></button>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 1rem; flex: 1;">
                <strong style="color: var(--text-primary);">Alias Tarjetas:</strong><br>
                <span style="display: inline-block; margin-top: 0.3rem;">${aliasesList}</span>
            </div>
            <div style="display: flex; gap: 0.5rem; margin-top: auto;">
                <input type="text" id="new-alias-${u.id}" placeholder="Nuevo Alias..." style="flex: 1; padding: 0.5rem; border-radius: 4px; border: 1px solid var(--glass-border); background: rgba(0,0,0,0.2); color: white; font-size: 0.85rem;">
                <button type="button" class="btn-secondary" onclick="addUserAlias('${u.id}')" style="padding: 0.5rem; font-size: 0.85rem;"><i class="fa-solid fa-plus"></i></button>
            </div>
        `;
        usersListContainer.appendChild(div);
    });
};

// Cards Functions
const saveCards = () => {
    localStorage.setItem('balance_cards', JSON.stringify(cardsConfig));
    populateCardSelects();
    renderCardsSettings();
    renderApp();
};

const populateCardSelects = () => {
    if (expenseCard) {
        expenseCard.innerHTML = '';
        cardsConfig.forEach(c => {
            const opt = document.createElement('option');
            opt.value = c.name;
            opt.textContent = c.name;
            expenseCard.appendChild(opt);
        });
    }

    if (filterCard) {
        const currentFilter = filterCard.value;
        filterCard.innerHTML = `
            <option value="all">Todos los Medios</option>
            <option value="cards">Todas las tarjetas</option>
            <option value="visa">Cualquier Visa</option>
            <option value="master">Cualquier Mastercard</option>
            <option value="efectivo">Cualquier Efectivo/Débito</option>
            <option disabled>--- Específicos ---</option>
        `;
        cardsConfig.forEach(c => {
            const opt = document.createElement('option');
            opt.value = c.name;
            opt.textContent = c.name;
            filterCard.appendChild(opt);
        });
        if (Array.from(filterCard.options).some(o => o.value === currentFilter)) {
            filterCard.value = currentFilter;
        }
    }
};

const renderCardsSettings = () => {
    if (!cardsListContainer) return;
    cardsListContainer.innerHTML = '';
    cardsConfig.forEach((c) => {
        const div = document.createElement('div');
        div.className = 'glassmorphism';
        div.style.padding = '1.2rem';
        div.style.background = 'rgba(255,255,255,0.05)';
        div.style.border = '1px solid var(--glass-border)';
        div.style.borderRadius = '8px';
        div.style.display = 'flex';
        div.style.flexDirection = 'column';
        
        let typeBadge = 'badge-efectivo';
        if (c.type === 'visa') typeBadge = 'badge-visa';
        if (c.type === 'master') typeBadge = 'badge-mastercard';
        if (c.type === 'mercado') typeBadge = 'badge-mercadopago';
        if (c.type === 'impuestos') typeBadge = 'badge-impuestos';

        let badgeStyle = '';
        if (c.type === 'mercado') badgeStyle = 'style="background-color: #009ee3; color: white; border-color: #009ee3;"';
        if (c.type === 'impuestos') badgeStyle = 'style="background-color: #8b5cf6; color: white; border-color: #8b5cf6;"';
        
        const aliasesList = (c.aliases || []).join(', ') || 'Sin alias';
        
        div.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.8rem;">
                <div>
                    <strong style="font-size: 1.1rem; color: var(--accent-primary); display: block; margin-bottom: 0.3rem;">${c.name}</strong>
                    <span class="badge ${typeBadge}" ${badgeStyle}>${c.type.toUpperCase()}</span>
                </div>
                <button class="btn-icon" onclick="deleteCard('${c.id}')" style="color: var(--danger);" title="Eliminar Tarjeta"><i class="fa-solid fa-trash"></i></button>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 1rem; flex: 1;">
                <strong style="color: var(--text-primary);">Alias importación:</strong><br>
                <span style="display: inline-block; margin-top: 0.3rem;">${aliasesList}</span>
            </div>
            <div style="display: flex; gap: 0.5rem; margin-top: auto;">
                <input type="text" id="new-card-alias-${c.id}" placeholder="Nuevo Alias (Ej. Visa)" style="flex: 1; padding: 0.5rem; border-radius: 4px; border: 1px solid var(--glass-border); background: rgba(0,0,0,0.2); color: white; font-size: 0.85rem;">
                <button type="button" class="btn-secondary" onclick="addCardAlias('${c.id}')" style="padding: 0.5rem; font-size: 0.85rem;"><i class="fa-solid fa-plus"></i></button>
            </div>
        `;
        cardsListContainer.appendChild(div);
    });
};

// Core Functions
const saveIncomes = () => {
    localStorage.setItem('balance_incomes', JSON.stringify(incomes));
};

const getMonthlyIncomes = (monthKey) => {
    let currentMonthIncomes = [];
    let recurringTracker = {}; // track latest recurring income per source
    let archivedTracker = [];
    
    // Sort incomes chronologically
    const sortedIncomes = [...incomes].sort((a, b) => a.monthKey.localeCompare(b.monthKey));

    sortedIncomes.forEach(inc => {
        if (inc.monthKey > monthKey) return; // Ignore future incomes

        if (inc.isRecurring) {
            if (inc.isArchived) {
                // If it is archived, it applies from monthKey to endMonthKey
                if (inc.endMonthKey >= monthKey) {
                    archivedTracker.push(inc);
                }
            } else {
                // Update latest recurring income for this source up to current month
                recurringTracker[inc.source] = inc;
            }
        }
        
        if (inc.monthKey === monthKey && !inc.isRecurring) {
            // Add one-off incomes for THIS month
            currentMonthIncomes.push(inc);
        }
    });

    // Add the active recurring incomes to the current month's list
    Object.values(recurringTracker).forEach(inc => {
        // We clone it to not mutate original if we need to add UI flags
        currentMonthIncomes.push({...inc, appliedFromRecurring: inc.monthKey !== monthKey});
    });
    
    archivedTracker.forEach(inc => {
        currentMonthIncomes.push({...inc, appliedFromRecurring: inc.monthKey !== monthKey});
    });

    return currentMonthIncomes;
};

window.deleteIncome = (id) => {
    if (confirm('¿Estás seguro de eliminar este ingreso?')) {
        incomes = incomes.filter(inc => inc.id !== id);
        saveIncomes();
        renderApp();
        if (typeof renderArchive === 'function' && document.getElementById('view-archive') && !document.getElementById('view-archive').classList.contains('hidden')) {
            renderArchive();
        }
        if (activeProjectId && !projectDetailModal.classList.contains('hidden')) {
            openProjectDetail(activeProjectId);
        }
    }
};

window.archiveIncome = (id) => {
    activeArchiveIncomeId = id;
    const inc = incomes.find(i => i.id === id);
    if (!inc) return;
    archiveIncomeEndMonth.value = getMonthKey(currentDate);
    archiveIncomeModal.classList.remove('hidden');
};

window.unarchiveIncome = (id) => {
    const inc = incomes.find(i => i.id === id);
    if (inc) {
        inc.isArchived = false;
        inc.endMonthKey = null;
        saveIncomes();
        renderApp();
        if (typeof renderArchive === 'function' && document.getElementById('view-archive') && !document.getElementById('view-archive').classList.contains('hidden')) {
            renderArchive();
        }
    }
};

if (document.getElementById('close-archive-income-modal')) {
    document.getElementById('close-archive-income-modal').addEventListener('click', () => archiveIncomeModal.classList.add('hidden'));
}
if (document.getElementById('btn-cancel-archive-income')) {
    document.getElementById('btn-cancel-archive-income').addEventListener('click', () => archiveIncomeModal.classList.add('hidden'));
}
if (document.getElementById('archive-income-form')) {
    document.getElementById('archive-income-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const endMonth = archiveIncomeEndMonth.value;
        if (!endMonth) return;
        
        const inc = incomes.find(i => i.id === activeArchiveIncomeId);
        if (inc) {
            inc.isArchived = true;
            inc.endMonthKey = endMonth;
            saveIncomes();
            renderApp();
            if (typeof renderArchive === 'function' && document.getElementById('view-archive') && !document.getElementById('view-archive').classList.contains('hidden')) {
                renderArchive();
            }
        }
        archiveIncomeModal.classList.add('hidden');
    });
}

const renderApp = () => {
    // 1. Update Month Display
    currentMonthDisplay.textContent = getMonthName(currentDate);
    const currentKey = getMonthKey(currentDate);
    
    renderWorkshopStatus();

    // 2. Filter expenses for current month
    let monthlyExpenses = expenses.filter(ex => ex.monthKey === currentKey);

    // 2.1 Apply UI Filters
    if (filterTitular && filterTitular.value !== 'all') {
        monthlyExpenses = monthlyExpenses.filter(ex => ex.titular === filterTitular.value);
    }
    if (filterCard && filterCard.value !== 'all') {
        const val = filterCard.value;
        if (val === 'cards') {
            monthlyExpenses = monthlyExpenses.filter(ex => {
                const cType = getCardTypeByName(ex.card);
                return cType === 'visa' || cType === 'master' || cType === 'mercado';
            });
        } else if (val === 'visa' || val === 'master' || val === 'mercado' || val === 'impuestos' || val === 'efectivo') {
            monthlyExpenses = monthlyExpenses.filter(ex => getCardTypeByName(ex.card) === val);
        } else {
            monthlyExpenses = monthlyExpenses.filter(ex => ex.card === val);
        }
    }
    if (filterType && filterType.value !== 'all') {
        if (filterType.value === 'one') monthlyExpenses = monthlyExpenses.filter(ex => !ex.installmentInfo && !ex.is_tax);
        if (filterType.value === 'installments') monthlyExpenses = monthlyExpenses.filter(ex => ex.installmentInfo && !ex.is_tax);
        if (filterType.value === 'tax') monthlyExpenses = monthlyExpenses.filter(ex => ex.is_tax);
        if (filterType.value === 'project') monthlyExpenses = monthlyExpenses.filter(ex => ex.projectId && (ex.projectId !== 'SHARED' || (ex.sharedProjectIds && ex.sharedProjectIds.length > 0) || ex.projectId === 'TO_ASSIGN'));
    }

    // 3. Calculate Expense Totals
    const total = monthlyExpenses.reduce((acc, curr) => acc + curr.amount, 0);
    const totalVisa = monthlyExpenses.filter(e => getCardTypeByName(e.card) === 'visa').reduce((acc, curr) => acc + curr.amount, 0);
    const totalMaster = monthlyExpenses.filter(e => getCardTypeByName(e.card) === 'master').reduce((acc, curr) => acc + curr.amount, 0);
    const totalOthers = total - totalVisa - totalMaster;

    if(totalExpenses) totalExpenses.textContent = formatCurrency(total);

    // 3.1 Calculate Incomes and Balance
    let monthlyIncomes = getMonthlyIncomes(currentKey);
    
    if (filterIncomeType && filterIncomeType.value !== 'all') {
        if (filterIncomeType.value === 'project') monthlyIncomes = monthlyIncomes.filter(inc => inc.projectId);
        if (filterIncomeType.value === 'recurring') monthlyIncomes = monthlyIncomes.filter(inc => inc.isRecurring);
        if (filterIncomeType.value === 'one') monthlyIncomes = monthlyIncomes.filter(inc => !inc.isRecurring);
    }

    const sumIncomes = monthlyIncomes.reduce((acc, curr) => acc + curr.amount, 0);
    const balance = sumIncomes - total;

    if(totalIncomes) totalIncomes.textContent = formatCurrency(sumIncomes);
    if(totalBalance) {
        totalBalance.textContent = formatCurrency(balance);
        if (balance >= 0) {
            totalBalance.style.color = '#3b82f6';
            balanceCard.style.boxShadow = '0 8px 32px 0 rgba(59, 130, 246, 0.15)';
            balanceCard.style.border = '1px solid rgba(59, 130, 246, 0.3)';
        } else {
            totalBalance.style.color = '#1d4ed8';
            balanceCard.style.boxShadow = '0 8px 32px 0 rgba(29, 78, 216, 0.15)';
            balanceCard.style.border = '1px solid rgba(29, 78, 216, 0.3)';
        }
    }

    // 3.2 Render Incomes Table
    if (incomeList) {
        incomeList.innerHTML = '';
        if (monthlyIncomes.length === 0) {
            incomeList.innerHTML = '<tr><td colspan="6" style="text-align: center; color: var(--text-secondary);">No hay ingresos registrados en este mes.</td></tr>';
        } else {
            // Sort by amount desc
            monthlyIncomes.sort((a, b) => b.amount - a.amount);
            monthlyIncomes.forEach(inc => {
                const tr = document.createElement('tr');
                
                let sourceBadge = 'badge-efectivo';
                if (inc.source === 'Escuela') sourceBadge = 'badge-visa';
                if (inc.source === 'Taller') sourceBadge = 'badge-mastercard';

                let actionHtml = '';
                if (inc.isRecurring && !inc.isArchived) {
                    actionHtml += `<button class="btn-icon" onclick="archiveIncome('${inc.id}')" title="Archivar Ingreso" style="color: var(--text-secondary); margin-right: 0.5rem;"><i class="fa-solid fa-box-archive"></i></button>`;
                }
                actionHtml += `<button class="btn-icon" onclick="deleteIncome('${inc.id}')" title="Eliminar Ingreso" style="color: var(--danger);"><i class="fa-solid fa-trash"></i></button>`;

                let projectNameHtml = '';
                if (inc.projectId) {
                    const project = projects.find(p => p.id === inc.projectId);
                    if (project) {
                        projectNameHtml = `<div style="font-size: 0.8rem; color: var(--accent-primary); margin-top: 0.2rem;"><i class="fa-solid fa-hammer"></i> ${project.name}</div>`;
                    }
                }

                tr.innerHTML = `
                    <td><span class="badge ${sourceBadge}">${inc.source}</span></td>
                    <td><strong>${inc.desc}</strong>${projectNameHtml}</td>
                    <td>${inc.titular || 'Raúl'}</td>
                    <td>${inc.isRecurring ? (inc.isArchived ? '<span style="color:var(--text-secondary);"><i class="fa-solid fa-box-archive"></i> Archivado (' + inc.monthKey + ' a ' + inc.endMonthKey + ')</span>' : '<i class="fa-solid fa-infinity" style="color:var(--success);"></i> Sí') : 'Solo este mes'}</td>
                    <td style="font-weight: 600; color: var(--success);">${formatCurrency(inc.amount)}</td>
                    <td>
                        ${actionHtml}
                    </td>
                `;
                incomeList.appendChild(tr);
            });
        }
    }

    // 4. Render Expenses Table
    expenseList.innerHTML = '';
    
    if (monthlyExpenses.length === 0) {
        emptyState.classList.remove('hidden');
        expenseTable.classList.add('hidden');
        if(expenseTableFooter) expenseTableFooter.classList.add('hidden');
    } else {
        emptyState.classList.add('hidden');
        expenseTable.classList.remove('hidden');
        if(expenseTableFooter) expenseTableFooter.classList.remove('hidden');
        
        if(tableFooterTotal) tableFooterTotal.textContent = formatCurrency(total);

        // Sort by titular, card, type (cuotas, un pago, tax), then desc
        monthlyExpenses.sort((a, b) => {
            const titularCmp = (a.titular || '').localeCompare(b.titular || '');
            if (titularCmp !== 0) return titularCmp;
            
            const cardCmp = (a.card || '').localeCompare(b.card || '');
            if (cardCmp !== 0) return cardCmp;
            
            const getTypeVal = (ex) => ex.is_tax ? 3 : (ex.installmentInfo ? 1 : 2);
            const typeA = getTypeVal(a);
            const typeB = getTypeVal(b);
            if (typeA !== typeB) return typeA - typeB;
            
            return (a.desc || '').localeCompare(b.desc || '');
        });

        monthlyExpenses.forEach(expense => {
            const tr = document.createElement('tr');
            
            // Badge color based on card
            const cType = getCardTypeByName(expense.card);
            let badgeClass = 'badge-efectivo';
            if (cType === 'visa') badgeClass = 'badge-visa';
            if (cType === 'master') badgeClass = 'badge-mastercard';
            if (cType === 'mercado') badgeClass = 'badge-mercadopago';
            if (cType === 'impuestos') badgeClass = 'badge-impuestos';

            let badgeStyle = '';
            if (cType === 'mercado') badgeStyle = 'style="background-color: #009ee3; color: white; border-color: #009ee3;"';
            if (cType === 'impuestos') badgeStyle = 'style="background-color: #8b5cf6; color: white; border-color: #8b5cf6;"';

            // Row classes based on type
            let rowClass = 'row-one-payment';
            if (expense.installmentInfo) rowClass = 'row-installments';
            if (expense.titular === 'Milagros') rowClass = 'row-milagros';
            if (expense.is_tax) rowClass = 'row-tax';
            if (expense.is_adjustment) rowClass = 'row-adjustment';
            
            tr.className = rowClass;

            let amountColor = expense.amount < 0 ? 'var(--success)' : 'inherit';

            let projectNameHtml = '';
            if (expense.projectId && expense.projectId !== 'SHARED') {
                const project = projects.find(p => p.id === expense.projectId);
                if (project) {
                    projectNameHtml = `<div style="font-size: 0.8rem; color: var(--accent-primary); margin-top: 0.2rem;"><i class="fa-solid fa-hammer"></i> ${project.name}</div>`;
                }
            } else if (expense.projectId === 'SHARED') {
                const count = expense.sharedProjectIds ? expense.sharedProjectIds.length : 0;
                projectNameHtml = `<div style="font-size: 0.8rem; color: var(--accent-primary); margin-top: 0.2rem;"><i class="fa-solid fa-layer-group"></i> Compartido (${count} proy.)</div>`;
            } else if (expense.projectId === 'TO_ASSIGN') {
                projectNameHtml = `<div style="font-size: 0.8rem; color: #f59e0b; margin-top: 0.2rem;"><i class="fa-solid fa-boxes-stacked"></i> En Inventario</div>`;
            }

            tr.innerHTML = `
                <td>${formatDateDisplay(expense.date)}</td>
                <td><strong>${expense.desc}</strong>${projectNameHtml}</td>
                <td><span class="badge ${badgeClass}" ${badgeStyle}>${expense.card}</span></td>
                <td>${expense.titular || 'Raúl'}</td>
                <td>${expense.installmentInfo || 'Un pago'}</td>
                <td style="font-weight: 600; color: ${amountColor};">${formatCurrency(expense.amount)}</td>
                <td>
                    <button class="btn-icon" onclick="toggleExpenseSign('${expense.groupId}')" title="Convertir en Devolución/Gasto" style="color: var(--accent-primary); margin-right: 8px;">
                        <i class="fa-solid fa-right-left"></i>
                    </button>
                    <button class="btn-icon" onclick="deleteExpense('${expense.groupId}')" title="Eliminar Gasto">
                        <i class="fa-solid fa-trash"></i>
                    </button>
                </td>
            `;
            expenseList.appendChild(tr);
        });
    }

    // 5. Update Chart
    updateChart(monthlyExpenses, sumIncomes, balance);
};

const updateChart = (monthlyExpenses, sumIncomes, balance) => {
    const ctx = document.getElementById('expenses-chart');
    if (!ctx) return;

    // Grouping Logic
    const totalExp = monthlyExpenses.reduce((acc, curr) => acc + curr.amount, 0);
    const groups = {};
    const groupTypes = {};
    monthlyExpenses.forEach(ex => {
        let groupName = 'Otros';
        let cType = getCardTypeByName(ex.card);

        if (ex.is_tax) {
            groupName = 'Mantenimiento / Impuestos';
            cType = 'impuestos';
        } else {
            groupName = `${ex.titular || 'Raúl'} - ${ex.card}`;
        }

        if (!groups[groupName]) {
            groups[groupName] = 0;
            groupTypes[groupName] = cType;
        }
        groups[groupName] += ex.amount;
    });

    const expenseLabels = Object.keys(groups);
    const expenseData = Object.values(groups);
    
    const labels = ['Ingresos Totales', 'Gastos Totales', 'Saldo Neto', ...expenseLabels];
    const data = [sumIncomes, totalExp, balance, ...expenseData];
    
    const backgroundColors = [
        'rgba(16, 185, 129, 0.8)', // Green for incomes
        'rgba(239, 68, 68, 0.9)', // Red for total expenses
        'rgba(59, 130, 246, 0.8)', // Blue for balance
        ...expenseLabels.map(label => {
            if (label === 'Mantenimiento / Impuestos') return 'rgba(153, 27, 27, 0.6)'; // Red-800
            if (label.includes('Milagros')) return 'rgba(248, 113, 113, 0.6)'; // Red-400
        
            const cType = groupTypes[label];
            if (cType === 'visa') return 'rgba(220, 38, 38, 0.6)'; // Red-600
            if (cType === 'master') return 'rgba(239, 68, 68, 0.6)'; // Red-500
            if (cType === 'mercado') return 'rgba(185, 28, 28, 0.6)'; // Red-700
            if (cType === 'impuestos') return 'rgba(127, 29, 29, 0.6)'; // Red-900
            return 'rgba(254, 202, 202, 0.6)'; // Red-200
        })
    ];

    if (expensesChartInstance) {
        if (expensesChartInstance.config.type !== 'bar') {
            expensesChartInstance.destroy();
            expensesChartInstance = null;
        }
    }

    if (!expensesChartInstance) {
        expensesChartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Monto ($)',
                    data: data,
                    backgroundColor: backgroundColors,
                    borderWidth: 0,
                    borderRadius: 4
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                layout: {
                    padding: { right: 60 }
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(context.parsed.x);
                            }
                        }
                    },
                    datalabels: {
                        color: '#f8fafc',
                        anchor: 'end',
                        align: 'end',
                        offset: 4,
                        font: {
                            weight: 'bold',
                            size: 12,
                            family: "'Outfit', sans-serif"
                        },
                        formatter: (value) => {
                            return new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(value);
                        }
                    }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        grid: { color: 'rgba(255,255,255,0.05)' },
                        ticks: { color: '#94a3b8' }
                    },
                    y: {
                        grid: { display: false },
                        ticks: { color: '#f8fafc', font: { family: "'Outfit', sans-serif", size: 12, weight: 'bold' } }
                    }
                }
            }
        });
    } else {
        expensesChartInstance.data.labels = labels;
        expensesChartInstance.data.datasets[0].data = data;
        expensesChartInstance.data.datasets[0].backgroundColor = backgroundColors;
        expensesChartInstance.update();
    }
};

const saveExpenses = () => {
    localStorage.setItem('balance_expenses', JSON.stringify(expenses));
    renderApp();
};

window.deleteExpense = (groupId) => {
    if(confirm('¿Estás seguro de que deseas eliminar este gasto y todas sus cuotas futuras?')) {
        expenses = expenses.filter(ex => ex.groupId !== groupId);
        saveExpenses();
    }
};

window.toggleExpenseSign = (groupId) => {
    expenses = expenses.map(ex => {
        if (ex.groupId === groupId) {
            return { ...ex, amount: -ex.amount };
        }
        return ex;
    });
    saveExpenses();
};

// Modal Handlers
const openModal = () => {
    modalOverlay.classList.remove('hidden');
    // Set default date to today
    document.getElementById('expense-date').valueAsDate = new Date();
    // Default start month to the currently viewed month
    document.getElementById('expense-start-month').value = getMonthKey(currentDate);

    const expenseProjectContainer = document.getElementById('expense-project-container');
    if (expenseProjectContainer) {
        expenseProjectContainer.innerHTML = `
            <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer; padding-bottom: 0.5rem; border-bottom: 1px solid rgba(255,255,255,0.05); margin-bottom: 0.2rem;">
                <input type="checkbox" class="expense-project-cb" value="TO_ASSIGN" style="width: 18px; height: 18px;">
                <span style="color: #f59e0b; font-weight: bold;">-- Enviar a Inventario / Pendiente --</span>
            </label>
        `;
        projects.slice().sort((a, b) => (a.name || '').localeCompare(b.name || '')).forEach(p => {
            if (!p.isArchived) {
                expenseProjectContainer.innerHTML += `
                    <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer;">
                        <input type="checkbox" class="expense-project-cb" value="${p.id}" style="width: 18px; height: 18px;">
                        <span>${p.name}</span>
                    </label>
                `;
            }
        });
    }
};

const closeModal = () => {
    modalOverlay.classList.add('hidden');
    expenseForm.reset();
};

window.openIncomeForProject = () => {
    returnToProjectId = activeProjectId;
    projectDetailModal.classList.add('hidden');
    openIncomeModal();
    if (incomeSource) {
        incomeSource.value = 'Taller';
        incomeSource.dispatchEvent(new Event('change'));
    }
    if (incomeProject) incomeProject.value = returnToProjectId;
};

window.openExpenseForProject = () => {
    returnToProjectId = activeProjectId;
    projectDetailModal.classList.add('hidden');
    openModal();
    
    const cbs = document.querySelectorAll('.expense-project-cb');
    cbs.forEach(cb => {
        cb.checked = cb.value === returnToProjectId;
    });
};

btnAddExpense.addEventListener('click', openModal);
btnCloseModal.addEventListener('click', () => { closeModal(); if (returnToProjectId) { openProjectDetail(returnToProjectId); returnToProjectId = null; } });
btnCancel.addEventListener('click', () => { closeModal(); if (returnToProjectId) { openProjectDetail(returnToProjectId); returnToProjectId = null; } });

// --- RENDER COMPARE VIEW ---
// --- RENDER COMPARE VIEW ---
const renderCompare = () => {
    const allMonthsSet = new Set();
    
    // 1. Group expenses
    const monthlyExpensesCards = {};
    const monthlyExpensesCash = {};

    allMonthsSet.add(getMonthKey(currentDate));

    expenses.forEach(ex => {
        if (!monthlyExpensesCards[ex.monthKey]) monthlyExpensesCards[ex.monthKey] = 0;
        if (!monthlyExpensesCash[ex.monthKey]) monthlyExpensesCash[ex.monthKey] = 0;
        
        const cType = getCardTypeByName(ex.card);
        const isCards = cType === 'visa' || cType === 'master' || cType === 'mercado';
        
        if (isCards) {
            monthlyExpensesCards[ex.monthKey] += ex.amount;
        } else {
            monthlyExpensesCash[ex.monthKey] += ex.amount;
        }
        
        allMonthsSet.add(ex.monthKey);
    });

    // Add incomes months to the set
    incomes.forEach(inc => {
        allMonthsSet.add(inc.monthKey);
    });

    let sortedMonths = Array.from(allMonthsSet).sort();
    if (sortedMonths.length === 0) return;

    // Evaluate incomes/expenses for all those months
    const monthlyIncomesTotals = {};
    const monthlyExpensesTotals = {};

    sortedMonths.forEach(m => {
        const monthIncomes = getMonthlyIncomes(m);
        monthlyIncomesTotals[m] = monthIncomes.reduce((sum, inc) => sum + inc.amount, 0);
        monthlyExpensesTotals[m] = (monthlyExpensesCards[m] || 0) + (monthlyExpensesCash[m] || 0);
    });
    
    // Eliminar meses que no tengan datos reales
    sortedMonths = sortedMonths.filter(m => monthlyIncomesTotals[m] !== 0 || monthlyExpensesTotals[m] !== 0);

    if (sortedMonths.length === 0) {
        if (compareChartInstance) {
            compareChartInstance.destroy();
            compareChartInstance = null;
        }
        if (compareMaxMonth) compareMaxMonth.textContent = "-";
        if (compareMaxAmount) compareMaxAmount.textContent = "$0.00";
        if (compareTrendPast) compareTrendPast.textContent = "-";
        if (compareTrendFuture) compareTrendFuture.textContent = "-";
        return;
    }

    // Stats calculation
    let maxMonthAmount = 0;
    let maxMonthKey = '';
    let maxChartValue = 0;
    
    sortedMonths.forEach(m => {
        const expAmount = monthlyExpensesTotals[m];
        const incAmount = monthlyIncomesTotals[m];
        
        if (expAmount > maxMonthAmount) {
            maxMonthAmount = expAmount;
            maxMonthKey = m;
        }
        
        const highestInMonth = Math.max(expAmount, incAmount);
        if (highestInMonth > maxChartValue) {
            maxChartValue = highestInMonth;
        }
    });

    const chartTopValue = maxChartValue > 0 ? maxChartValue * 1.1 : 1000;

    // --- NEW TREND LOGIC ---
    const selectedMonthKey = getMonthKey(currentDate);
    const selectedIdx = sortedMonths.indexOf(selectedMonthKey);

    // 1. Tendencia Tarjeta: Difference in TARJETAS vs PREVIOUS Month
    let trendPastText = "-";
    let trendPastColor = "var(--text-secondary)";
    let trendPastDesc = "No hay datos del mes anterior";

    if (selectedIdx > 0) {
        const prevMonthKey = sortedMonths[selectedIdx - 1];
        
        const currentCards = monthlyExpensesCards[selectedMonthKey] || 0;
        const prevCards = monthlyExpensesCards[prevMonthKey] || 0;
        const diffCards = currentCards - prevCards;

        if (diffCards > 1) {
            trendPastText = `+${formatCurrency(diffCards)}`;
            trendPastColor = "var(--danger)"; 
        } else if (diffCards < -1) {
            trendPastText = `${formatCurrency(diffCards)}`;
            trendPastColor = "var(--success)"; 
        } else {
            trendPastText = "$0.00";
            trendPastColor = "var(--text-primary)";
        }
        trendPastDesc = `vs Tarjetas de ${getMonthName(new Date(prevMonthKey + '-15'))}`;
    }

    // 2. Future Comparison: SUM of all following expenses
    let trendFutureText = "-";
    let trendFutureColor = "var(--text-secondary)";
    let trendFutureDesc = "No hay gastos futuros";

    if (selectedIdx !== -1 && selectedIdx < sortedMonths.length - 1) {
        const futureMonths = sortedMonths.slice(selectedIdx + 1);
        const futureExpTotal = futureMonths.reduce((sum, m) => sum + monthlyExpensesTotals[m], 0);
        
        trendFutureText = formatCurrency(futureExpTotal);
        trendFutureColor = "var(--danger)";
        trendFutureDesc = `Suma de ${futureMonths.length} meses siguientes`;
    }

    // Update UI Cards
    if (compareMonthDisplay) compareMonthDisplay.textContent = getMonthName(currentDate);

    if (compareMaxMonth) {
        if (maxMonthKey) {
            let [y, mo] = maxMonthKey.split('-');
            let date = new Date(y, parseInt(mo)-1, 1);
            compareMaxMonth.textContent = getMonthName(date);
            if (compareMaxAmount) compareMaxAmount.textContent = formatCurrency(maxMonthAmount);
        }
    }

    if (compareTrendPast) {
        compareTrendPast.textContent = trendPastText;
        compareTrendPast.style.color = trendPastColor;
        if (compareTrendPastDesc) compareTrendPastDesc.textContent = trendPastDesc;
    }

    if (compareTrendFuture) {
        compareTrendFuture.textContent = trendFutureText;
        compareTrendFuture.style.color = trendFutureColor;
        if (compareTrendFutureDesc) compareTrendFutureDesc.textContent = trendFutureDesc;
    }

    // --- CHART DATA (Sliding window) ---
    const monthsToShow = window.innerWidth <= 768 ? 2 : 12;

    // Initialize chartStartIndex if not set or if we want to reset to current month focus
    if (chartStartIndex === null) {
        chartStartIndex = selectedIdx !== -1 ? selectedIdx : Math.max(0, sortedMonths.length - monthsToShow);
    }

    // Ensure chartStartIndex is within bounds
    chartStartIndex = Math.max(0, Math.min(chartStartIndex, sortedMonths.length - 1));

    // Slice months starting from chartStartIndex
    const chartMonths = sortedMonths.slice(chartStartIndex, chartStartIndex + monthsToShow);

    // Update Navigation Buttons state (the ones on the chart)
    if (btnChartPrev) btnChartPrev.disabled = (chartStartIndex <= 0);
    if (btnChartNext) btnChartNext.disabled = (chartStartIndex + monthsToShow >= sortedMonths.length);

    // Update Chart
    const chartContainer = document.getElementById('compare-chart-container');
    if (chartContainer) {
        chartContainer.style.width = '100%'; 
    }

    const ctx = document.getElementById('compare-bar-chart');
    if (!ctx) return;

    const labels = chartMonths.map((m, index) => {
        let [y, mo] = m.split('-');
        let d = new Date(y, parseInt(mo)-1, 1);
        return [getMonthName(d), `(${index + 1})`];
    });
    const dataCards = chartMonths.map(m => monthlyExpensesCards[m] || 0);
    const dataCash = chartMonths.map(m => monthlyExpensesCash[m] || 0);
    const dataIncomes = chartMonths.map(m => monthlyIncomesTotals[m] || 0);
    const dataDummyTop = chartMonths.map(() => chartTopValue);

    if (compareChartInstance) {
        compareChartInstance.data.labels = labels;
        compareChartInstance.data.datasets[0].data = dataIncomes;
        compareChartInstance.data.datasets[1].data = dataCash;
        compareChartInstance.data.datasets[2].data = dataCards;
        if (compareChartInstance.data.datasets[3]) {
            compareChartInstance.data.datasets[3].data = dataDummyTop;
        }
        compareChartInstance.options.scales.y.suggestedMax = chartTopValue * 1.4;
        compareChartInstance.update();
    } else {
        compareChartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Ingresos Totales',
                        data: dataIncomes,
                        stack: 'stack0',
                        backgroundColor: 'rgba(16, 185, 129, 0.6)', // Green
                        borderColor: '#10b981',
                        borderWidth: 1,
                        borderRadius: 4,
                        datalabels: {
                            display: false // Text is rendered by the top stack dataset
                        }
                    },
                    {
                        label: 'Gastos Efectivo/Débito',
                        data: dataCash,
                        stack: 'stack1',
                        backgroundColor: 'rgba(248, 113, 113, 0.6)', // Red 400
                        borderColor: '#f87171',
                        borderWidth: 1,
                        borderRadius: { topLeft: 0, topRight: 0, bottomLeft: 4, bottomRight: 4 },
                        datalabels: {
                            display: false // No mostramos texto dentro de la barra
                        }
                    },
                    {
                        label: 'Gastos Tarjeta',
                        data: dataCards,
                        stack: 'stack1',
                        backgroundColor: 'rgba(220, 38, 38, 0.6)', // Red 600
                        borderColor: '#dc2626',
                        borderWidth: 1,
                        borderRadius: { topLeft: 4, topRight: 4, bottomLeft: 0, bottomRight: 0 },
                        datalabels: {
                            display: false
                        }
                    },
                    {
                        label: 'Etiquetas Superiores',
                        type: 'line',
                        data: dataDummyTop,
                        borderColor: 'transparent',
                        backgroundColor: 'transparent',
                        pointRadius: 0,
                        pointHoverRadius: 0,
                        datalabels: {
                            labels: {
                                entradas: {
                                    align: 'top', anchor: 'end', offset: 45,
                                    color: '#10b981',
                                    font: { size: 11, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => {
                                        const inc = ctx.chart.data.datasets[0].data[ctx.dataIndex];
                                        return `Ent: ${formatCurrency(inc)}`;
                                    }
                                },
                                gastos: {
                                    align: 'top', anchor: 'end', offset: 25,
                                    color: '#ef4444',
                                    font: { size: 11, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => {
                                        const card = ctx.chart.data.datasets[2].data[ctx.dataIndex];
                                        const cash = ctx.chart.data.datasets[1].data[ctx.dataIndex];
                                        const total = card + cash;
                                        return `Gto: ${formatCurrency(total)}`;
                                    }
                                },
                                saldo: {
                                    align: 'top', anchor: 'end', offset: 5,
                                    color: '#3b82f6',
                                    font: { size: 11, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => {
                                        const inc = ctx.chart.data.datasets[0].data[ctx.dataIndex];
                                        const card = ctx.chart.data.datasets[2].data[ctx.dataIndex];
                                        const cash = ctx.chart.data.datasets[1].data[ctx.dataIndex];
                                        const balance = inc - (card + cash);
                                        return `Sal: ${formatCurrency(balance)}`;
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        suggestedMax: chartTopValue * 1.4,
                        grid: { color: 'rgba(255,255,255,0.05)' },
                        ticks: { color: '#94a3b8' }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { 
                            color: '#94a3b8',
                            font: { size: 10 },
                            padding: 15
                        }
                    }
                },
                layout: {
                    padding: { top: 70 }
                },
                plugins: {
                    legend: { 
                        display: true, 
                        position: 'bottom',
                        labels: { color: '#94a3b8' }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS' }).format(context.parsed.y);
                            }
                        }
                    },
                    datalabels: { 
                        display: true,
                        color: '#f8fafc',
                        anchor: 'end',
                        align: 'end',
                        offset: 5,
                        font: {
                            weight: 'bold',
                            size: 13,
                            family: "'Outfit', sans-serif"
                        },
                        formatter: (value) => {
                            return new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(value);
                        }
                    }
                }
            }
        });
    }

    // --- BALANCE CALCULATOR ---
    if (compareBalancesContainer) {
        compareBalancesContainer.innerHTML = '';
        sortedMonths.forEach(m => {
            const inc = monthlyIncomesTotals[m] || 0;
            const exp = monthlyExpensesTotals[m] || 0;
            const bal = inc - exp;
            
            const chip = document.createElement('label');
            chip.style.display = 'flex';
            chip.style.alignItems = 'center';
            chip.style.gap = '0.5rem';
            chip.style.padding = '0.4rem 0.8rem';
            chip.style.borderRadius = '20px';
            chip.style.cursor = 'pointer';
            chip.style.border = '1px solid var(--glass-border)';
            chip.style.background = selectedCompareMonths.has(m) ? 'rgba(59, 130, 246, 0.2)' : 'rgba(255,255,255,0.05)';
            chip.style.transition = 'all 0.2s';
            chip.style.userSelect = 'none';
            
            if (selectedCompareMonths.has(m)) {
                chip.style.borderColor = 'rgba(59, 130, 246, 0.5)';
            }
            
            let [y, mo] = m.split('-');
            let d = new Date(y, parseInt(mo)-1, 15);
            const monthName = d.toLocaleDateString('es-AR', { month: 'short', year: '2-digit' });
            const balColor = bal >= 0 ? 'var(--success)' : 'var(--danger)';
            
            chip.innerHTML = `
                <input type="checkbox" value="${m}" class="compare-month-cb" data-balance="${bal}" style="display: none;" ${selectedCompareMonths.has(m) ? 'checked' : ''}>
                <span style="font-weight: 600; text-transform: capitalize; font-size: 0.85rem;">${monthName}</span>
                <span style="color: ${balColor}; font-weight: 700; font-size: 0.85rem;">${formatCurrency(bal)}</span>
            `;
            
            chip.querySelector('input').addEventListener('change', (e) => {
                if (e.target.checked) {
                    selectedCompareMonths.add(m);
                    chip.style.background = 'rgba(59, 130, 246, 0.2)';
                    chip.style.borderColor = 'rgba(59, 130, 246, 0.5)';
                } else {
                    selectedCompareMonths.delete(m);
                    chip.style.background = 'rgba(255,255,255,0.05)';
                    chip.style.borderColor = 'var(--glass-border)';
                }
                updateCompareSelectionSum();
            });
            
            compareBalancesContainer.appendChild(chip);
        });
        updateCompareSelectionSum();
    }
};

const updateCompareSelectionSum = () => {
    if (!compareSelectedSum) return;
    let total = 0;
    document.querySelectorAll('.compare-month-cb:checked').forEach(cb => {
        total += parseFloat(cb.dataset.balance);
    });
    compareSelectedSum.textContent = formatCurrency(total);
    if (total >= 0) {
        compareSelectedSum.style.color = '#3b82f6';
    } else {
        compareSelectedSum.style.color = '#ef4444';
    }
};

if (btnCompareSelectAll) {
    btnCompareSelectAll.addEventListener('click', () => {
        document.querySelectorAll('.compare-month-cb').forEach(cb => {
            if (!cb.checked) {
                cb.checked = true;
                cb.dispatchEvent(new Event('change'));
            }
        });
    });
}

if (btnCompareClearAll) {
    btnCompareClearAll.addEventListener('click', () => {
        document.querySelectorAll('.compare-month-cb:checked').forEach(cb => {
            cb.checked = false;
            cb.dispatchEvent(new Event('change'));
        });
    });
}

// --- SIMULATOR LOGIC ---
const renderSimulatedProjects = () => {
    if (!simProjectsList) return;
    simProjectsList.innerHTML = '';
    simulatedProjects.forEach((p, index) => {
        const div = document.createElement('div');
        div.className = 'glassmorphism';
        div.style.padding = '0.8rem';
        div.style.display = 'flex';
        div.style.justifyContent = 'space-between';
        div.style.alignItems = 'center';
        div.style.background = 'rgba(99, 102, 241, 0.1)';
        div.style.border = '1px solid rgba(99, 102, 241, 0.3)';
        
        div.innerHTML = `
            <div>
                <strong style="color: var(--accent-primary);">${p.name}</strong>
                <div style="font-size: 0.8rem; color: var(--text-secondary);">
                    Gasto: ${formatCurrency(p.cost)} (${p.installments} cuotas) | Ingreso: ${formatCurrency(p.income)}
                </div>
            </div>
            <button class="btn-icon" onclick="removeSimProject(${index})" style="color: var(--danger);">
                <i class="fa-solid fa-trash"></i>
            </button>
        `;
        simProjectsList.appendChild(div);
    });
};

window.removeSimProject = (index) => {
    simulatedProjects.splice(index, 1);
    renderSimulatedProjects();
    
    if (simulatedProjects.length === 0) {
        simResults.classList.add('hidden');
    } else if (!simResults.classList.contains('hidden')) {
        runSimulation(false);
    }
};

if (btnAddSimProject) {
    btnAddSimProject.addEventListener('click', () => {
        const name = simNameInput.value || 'Proyecto ' + (simulatedProjects.length + 1);
        const cost = parseFloat(simExpenseInput.value) || 0;
        const installments = parseInt(simInstallmentsInput.value) || 1;
        const expStart = simExpenseStartInput.value || getMonthKey(currentDate);
        const income = parseFloat(simIncomeInput.value) || 0;
        const incStart = simIncomeStartInput.value || getMonthKey(currentDate);
        const projMonths = parseInt(simProjectMonthsInput.value) || 12;
        const projId = simProjectSelect && simProjectSelect.value ? simProjectSelect.value : null;

        if (cost === 0 && income === 0 && !projId) {
            alert('Debes ingresar al menos un costo, un ingreso, o seleccionar un proyecto para simular.');
            return;
        }

        simulatedProjects.push({ id: 'sim_' + Date.now(), projectId: projId, name, cost, installments, expStart, income, incStart, projMonths });
        renderSimulatedProjects();
        
        simNameInput.value = '';
        simExpenseInput.value = '';
        simInstallmentsInput.value = '1';
        simIncomeInput.value = '';
        simProjectMonthsInput.value = '12';
        if (simProjectSelect) simProjectSelect.value = '';
    });
}

const addMonthsToKey = (key, delta) => {
    let [y, m] = key.split('-').map(Number);
    const d = new Date(y, m - 1 + delta, 15);
    return getMonthKey(d);
};

const runSimulation = (e) => {
    const isAutoAdd = (e instanceof Event) || (e === undefined) || (e === true);
    
    if (isAutoAdd) {
        // Auto-añadir si el usuario llenó los campos pero olvidó darle al botón "+"
        const currentCost = parseFloat(simExpenseInput.value) || 0;
        const currentIncome = parseFloat(simIncomeInput.value) || 0;
        if (currentCost > 0 || currentIncome > 0) {
            if (btnAddSimProject) btnAddSimProject.click();
        }
    }

    if (simulatedProjects.length === 0) {
        if (isAutoAdd) {
            alert('Por favor, añade al menos un proyecto a la lista de simulación antes de calcular.');
        }
        simResults.classList.add('hidden');
        return;
    }

    const simMonths = parseInt(simMonthsInput.value) || 12;

    let startKey = getMonthKey(currentDate);
    simulatedProjects.forEach(p => {
        if (p.expStart < startKey) startKey = p.expStart;
        if (p.income > 0 && p.incStart < startKey) startKey = p.incStart;
    });

    const months = [];
    for (let i = 0; i < simMonths; i++) {
        months.push(addMonthsToKey(startKey, i));
    }

    const labels = [];
    const baseIncSums = [];
    const totalIncSums = [];
    const baseExpSums = [];
    const totalExpSums = [];
    const simBalances = [];
    const baseBalances = [];

    months.forEach(mKey => {
        let baseIncSum = 0;
        let simIncSum = 0;

        const monthIncomes = getMonthlyIncomes(mKey);
        monthIncomes.forEach(inc => {
            if (inc.projectId && simulatedProjects.some(p => p.projectId === inc.projectId)) {
                simIncSum += inc.amount;
            } else {
                baseIncSum += inc.amount;
            }
        });

        let baseExpSum = 0;
        let simExpSum = 0;
        expenses.forEach(ex => {
            if (ex.monthKey === mKey) {
                let isSimulatedFull = ex.projectId && ex.projectId !== 'SHARED' && simulatedProjects.some(p => p.projectId === ex.projectId);
                let simulatedPortion = 0;
                
                if (ex.projectId === 'SHARED' && ex.sharedProjectIds && ex.sharedProjectIds.length > 0) {
                    const simProjCount = simulatedProjects.filter(p => ex.sharedProjectIds.includes(p.projectId)).length;
                    if (simProjCount > 0) {
                        simulatedPortion = (ex.amount / ex.sharedProjectIds.length) * simProjCount;
                    }
                }

                if (isSimulatedFull) {
                    simExpSum += ex.amount;
                } else if (simulatedPortion > 0) {
                    simExpSum += simulatedPortion;
                    baseExpSum += (ex.amount - simulatedPortion);
                } else {
                    baseExpSum += ex.amount;
                }
            }
        });

        const baseBal = baseIncSum - baseExpSum;

        simulatedProjects.forEach(p => {
            let [yE, mE] = p.expStart.split('-').map(Number);
            let expStartDate = new Date(yE, mE - 1, 15);
            let [yC, mC] = mKey.split('-').map(Number);
            let currentDateObj = new Date(yC, mC - 1, 15);

            let monthsDiffExp = (currentDateObj.getFullYear() - expStartDate.getFullYear()) * 12 + (currentDateObj.getMonth() - expStartDate.getMonth());
            if (monthsDiffExp >= 0 && monthsDiffExp < p.installments) {
                simExpSum += (p.installments > 0 ? p.cost / p.installments : 0);
            }

            let [yI, mI] = p.incStart.split('-').map(Number);
            let incStartDate = new Date(yI, mI - 1, 15);
            let monthsDiffInc = (currentDateObj.getFullYear() - incStartDate.getFullYear()) * 12 + (currentDateObj.getMonth() - incStartDate.getMonth());

            if (monthsDiffInc >= 0 && monthsDiffInc < p.projMonths && p.income > 0) {
                simIncSum += p.income;
            }
        });

        const totalInc = baseIncSum + simIncSum;
        const totalExp = baseExpSum + simExpSum;
        const simBal = totalInc - totalExp;

        let [y, mo] = mKey.split('-');
        const d = new Date(y, mo - 1, 15);
        labels.push(d.toLocaleDateString('es-AR', { month: 'short', year: '2-digit' })); 
        baseIncSums.push(baseIncSum);
        totalIncSums.push(totalInc);
        baseExpSums.push(baseExpSum);
        totalExpSums.push(totalExp);
        simBalances.push(simBal);
        baseBalances.push(baseBal);
    });

    // Análisis Final
    const totalBase = baseBalances.reduce((a, b) => a + b, 0);
    const totalSim = simBalances.reduce((a, b) => a + b, 0);
    const diff = totalSim - totalBase;

    const simSummaryText = document.getElementById('sim-summary-text');
    if (simSummaryText) {
        if (diff > 0) {
            simSummaryText.innerHTML = `En un horizonte de ${simMonths} meses, los proyectos sumarían a tus finanzas un <span style="color: var(--success); font-weight: 800;">saldo a favor de ${formatCurrency(diff)} adicionales</span> respecto a tu situación actual.`;
        } else if (diff < 0) {
            simSummaryText.innerHTML = `En un horizonte de ${simMonths} meses, los proyectos tendrían un <span style="color: var(--danger); font-weight: 800;">costo neto real de ${formatCurrency(Math.abs(diff))}</span> (amortizando gastos contra posibles ganancias).`;
        } else {
            simSummaryText.innerHTML = `El impacto se amortiza a la perfección. No altera tu balance neto final tras ${simMonths} meses.`;
        }
    }

    simResults.classList.remove('hidden');

    const simChartContainer = document.getElementById('simulator-chart-container');
    if (simChartContainer) {
        // Asigna un mínimo de 160px de ancho por cada mes para que las 6 barras y etiquetas entren perfectas
        const minWidth = Math.max(simMonths * 160, simChartContainer.parentElement.clientWidth);
        simChartContainer.style.width = `${minWidth}px`;
    }

    const ctx = document.getElementById('simulator-chart');
    if (!ctx) return;

    const maxVal = Math.max(...baseIncSums, ...totalIncSums, ...baseExpSums, ...totalExpSums, ...baseBalances, ...simBalances, 0);
    const dummyTopData = months.map(() => maxVal);
    const chartTopValue = maxVal > 0 ? maxVal * 1.2 : 1000;

    const baseBalancesBg = baseBalances.map(b => 'rgba(96, 165, 250, 0.6)'); // Blue 400
    const baseBalancesBorder = baseBalances.map(b => '#60a5fa');

    const simBalancesBg = simBalances.map(b => 'rgba(37, 99, 235, 0.8)'); // Blue 600
    const simBalancesBorder = simBalances.map(b => '#2563eb');

    if (simulatorChartInstance) {
        simulatorChartInstance.data.labels = labels;
        simulatorChartInstance.data.datasets[0].data = baseIncSums;
        simulatorChartInstance.data.datasets[1].data = totalIncSums;
        if (simulatorChartInstance.data.datasets[2]) {
            simulatorChartInstance.data.datasets[2].data = baseExpSums;
        }
        if (simulatorChartInstance.data.datasets[3]) {
            simulatorChartInstance.data.datasets[3].data = totalExpSums;
        }
        if (simulatorChartInstance.data.datasets[4]) {
            simulatorChartInstance.data.datasets[4].data = baseBalances;
            simulatorChartInstance.data.datasets[4].backgroundColor = baseBalancesBg;
            simulatorChartInstance.data.datasets[4].borderColor = baseBalancesBorder;
        }
        if (simulatorChartInstance.data.datasets[5]) {
            simulatorChartInstance.data.datasets[5].data = simBalances;
            simulatorChartInstance.data.datasets[5].backgroundColor = simBalancesBg;
            simulatorChartInstance.data.datasets[5].borderColor = simBalancesBorder;
        }
        if (simulatorChartInstance.data.datasets[6]) {
            simulatorChartInstance.data.datasets[6].data = dummyTopData;
        }
        simulatorChartInstance.options.scales.y.suggestedMax = chartTopValue * 1.1;
        simulatorChartInstance.update();
    } else {
        simulatorChartInstance = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Ingreso Real (Sin proyecto)',
                        data: baseIncSums,
                        backgroundColor: 'rgba(52, 211, 153, 0.6)',
                        borderColor: '#34d399',
                        borderWidth: 1,
                        borderRadius: 4,
                        datalabels: { display: false }
                    },
                    {
                        label: 'Ingreso Total (Con proyecto)',
                        data: totalIncSums,
                        backgroundColor: 'rgba(16, 185, 129, 0.9)',
                        borderColor: '#10b981',
                        borderWidth: 1,
                        borderRadius: 4,
                        datalabels: { display: false }
                    },
                    {
                        label: 'Gasto Real (Sin proyecto)',
                        data: baseExpSums,
                        backgroundColor: 'rgba(248, 113, 113, 0.6)',
                        borderColor: '#f87171',
                        borderWidth: 1,
                        borderRadius: 4,
                        datalabels: { display: false }
                    },
                    {
                        label: 'Gasto Total (Con proyecto)',
                        data: totalExpSums,
                        backgroundColor: 'rgba(239, 68, 68, 0.9)',
                        borderColor: '#ef4444',
                        borderWidth: 1,
                        borderRadius: 4,
                        datalabels: { display: false }
                    },
                    {
                        label: 'Balance Real (Sin proyecto)',
                        data: baseBalances,
                        backgroundColor: baseBalancesBg,
                        borderColor: baseBalancesBorder,
                        borderWidth: 1,
                        borderRadius: 4,
                        datalabels: { display: false }
                    },
                    {
                        label: 'Balance Total (Con proyecto)',
                        data: simBalances,
                        backgroundColor: simBalancesBg,
                        borderColor: simBalancesBorder,
                        borderWidth: 1,
                        borderRadius: 4,
                        datalabels: { display: false }
                    },
                    {
                        label: 'Etiquetas Superiores',
                        type: 'line',
                        data: dummyTopData,
                        borderColor: 'transparent',
                        backgroundColor: 'transparent',
                        pointRadius: 0,
                        pointHoverRadius: 0,
                        datalabels: {
                            display: true,
                            labels: {
                                inReal: {
                                    align: 'top', anchor: 'end', offset: 95,
                                    color: '#34d399',
                                    font: { size: 10, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => `+Real: ${formatCurrency(ctx.chart.data.datasets[0].data[ctx.dataIndex])}`
                                },
                                inProy: {
                                    align: 'top', anchor: 'end', offset: 80,
                                    color: '#10b981',
                                    font: { size: 10, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => `+Proy: ${formatCurrency(ctx.chart.data.datasets[1].data[ctx.dataIndex])}`
                                },
                                exReal: {
                                    align: 'top', anchor: 'end', offset: 65,
                                    color: '#f87171',
                                    font: { size: 10, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => `-Real: ${formatCurrency(ctx.chart.data.datasets[2].data[ctx.dataIndex])}`
                                },
                                exProy: {
                                    align: 'top', anchor: 'end', offset: 50,
                                    color: '#ef4444',
                                    font: { size: 10, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => `-Proy: ${formatCurrency(ctx.chart.data.datasets[3].data[ctx.dataIndex])}`
                                },
                                balReal: {
                                    align: 'top', anchor: 'end', offset: 35,
                                    color: '#60a5fa',
                                    font: { size: 10, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => `Bal R: ${formatCurrency(ctx.chart.data.datasets[4].data[ctx.dataIndex])}`
                                },
                                balProy: {
                                    align: 'top', anchor: 'end', offset: 20,
                                    color: '#2563eb',
                                    font: { size: 10, weight: 'bold', family: "'Outfit', sans-serif" },
                                    formatter: (v, ctx) => `Bal P: ${formatCurrency(ctx.chart.data.datasets[5].data[ctx.dataIndex])}`
                                }
                            }
                        }
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                layout: {
                    padding: { top: 135 }
                },
                plugins: {
                    legend: { 
                        position: 'bottom', 
                        labels: { color: '#f8fafc' },
                        filter: function(item) {
                            return item.text !== 'Etiquetas Superiores';
                        }
                    },
                    datalabels: { display: false },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                if (context.dataset.label === 'Etiquetas Superiores') return null;
                                return context.dataset.label + ': ' + formatCurrency(context.parsed.y);
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        suggestedMax: chartTopValue * 1.1,
                        grid: { color: 'rgba(255,255,255,0.05)' },
                        ticks: { color: '#94a3b8' }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { 
                            color: '#94a3b8',
                            font: { family: "'Outfit', sans-serif", size: 11 },
                            padding: 10
                        }
                    }
                }
            }
        });
    }
};

if (btnSimulate) {
    btnSimulate.addEventListener('click', runSimulation);
}

if (simProjectSelect) {
    simProjectSelect.addEventListener('change', (e) => {
        const projId = e.target.value;
        if (!projId) {
            if (simNameInput) simNameInput.value = '';
            if (simExpenseInput) simExpenseInput.value = '';
            if (simInstallmentsInput) simInstallmentsInput.value = '1';
            if (simExpenseStartInput) simExpenseStartInput.value = getMonthKey(currentDate);
            if (simIncomeStartInput) simIncomeStartInput.value = getMonthKey(currentDate);
            if (simIncomeInput) simIncomeInput.value = '';
            if (simProjectMonthsInput) simProjectMonthsInput.value = '12';
            return;
        }

        const project = projects.find(p => p.id === projId);
        if (project) {
            const extrasTotal = (project.extraExpenses || []).reduce((sum, e) => sum + parseFloat(e.amount), 0);
            const totalCost = extrasTotal;
            const expectedTotal = (project.expectedIncomes || []).reduce((sum, e) => sum + parseFloat(e.amount), 0);
            const expMos = parseInt(project.expectedMonths) || 12;

            if (simNameInput) simNameInput.value = project.name;
            if (simExpenseInput) simExpenseInput.value = totalCost;
            if (simInstallmentsInput) simInstallmentsInput.value = '1';
            const startKey = project.startDate ? project.startDate.substring(0, 7) : getMonthKey(currentDate);
            if (simExpenseStartInput) simExpenseStartInput.value = startKey;
            if (simIncomeStartInput) simIncomeStartInput.value = startKey;
            if (simIncomeInput) simIncomeInput.value = (expectedTotal / expMos).toFixed(2);
            if (simProjectMonthsInput) simProjectMonthsInput.value = expMos;
        }
    });
}

if (btnClearSim) {
    btnClearSim.addEventListener('click', () => {
        simulatedProjects = [];
        renderSimulatedProjects();
        simResults.classList.add('hidden');
    });
}

if (btnSaveSimProject) {
    btnSaveSimProject.addEventListener('click', () => {
        saveSimModal.classList.remove('hidden');
        simProjectTitle.value = simulatedProjects.length === 1 ? simulatedProjects[0].name : 'Proyectos Combinados';
        setTimeout(() => simProjectTitle.focus(), 100);
    });
}

const hideSaveSimModal = () => {
    saveSimModal.classList.add('hidden');
};

if (closeSaveSimModal) closeSaveSimModal.addEventListener('click', hideSaveSimModal);
if (btnCancelSaveSim) btnCancelSaveSim.addEventListener('click', hideSaveSimModal);

if (saveSimForm) {
    saveSimForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const title = simProjectTitle.value.trim();
        if (!title) return;

        if (simulatedProjects.length === 0) {
            alert("No hay proyectos en la simulación.");
            return;
        }
        
        let totalCost = 0;
        let totalIncome = 0;
        let earliestStart = getMonthKey(currentDate);
        
        simulatedProjects.forEach(p => {
            totalCost += p.cost;
            totalIncome += p.income;
            if (p.expStart < earliestStart) earliestStart = p.expStart;
        });
        
        const detailsMsg = `Proyecto combinado originado en Simulador (${simulatedProjects.length} sub-proyectos). Inversión total: ${formatCurrency(totalCost)}. Ingreso potencial: ${formatCurrency(totalIncome)}.`;

        const newProject = {
            id: 'proj_' + Date.now() + Math.random().toString(36).substr(2, 9),
            name: title,
            description: detailsMsg,
            status: 'en-proyecto',
            startDate: earliestStart + '-01',
            endDate: '',
            image: '',
            costMaterials: totalCost,
            costLabor: 0,
            hours: 0,
            hourlyRate: 0,
            processes: [
                {
                    name: "Análisis y Presupuesto (Simulador)",
                    completed: true,
                    completedAt: new Date().toLocaleString('es-AR'),
                    days: [],
                    deadlineDate: "",
                    startTime: "",
                    endTime: ""
                }
            ],
            schedules: [],
            history: [{ time: new Date().toLocaleString('es-AR'), msg: detailsMsg }],
            extraExpenses: [],
            photos: []
        };

        projects.push(newProject);
        saveProjects();
        renderWorkshop();

        hideSaveSimModal();
        alert(`¡El proyecto "${title}" ha sido guardado exitosamente en la sección Taller!`);
    });
}

// --- VIEW SWITCHING ---
const switchView = (viewName) => {
    viewDashboard.classList.add('hidden');
    viewCompare.classList.add('hidden');
    viewHistory.classList.add('hidden');
    viewWorkshop.classList.add('hidden');
    if(viewArchive) viewArchive.classList.add('hidden');
    if(viewStats) viewStats.classList.add('hidden');
    viewCash.classList.add('hidden');
    viewSettings.classList.add('hidden');
    if(viewHelp) viewHelp.classList.add('hidden');
    
    navDashboard.classList.remove('active');
    if(navCompare) navCompare.classList.remove('active');
    navHistory.classList.remove('active');
    if(navWorkshop) navWorkshop.classList.remove('active');
    if(navArchive) navArchive.classList.remove('active');
    if(navStats) navStats.classList.remove('active');
    if(navCash) navCash.classList.remove('active');
    navSettings.classList.remove('active');
    if(navHelp) navHelp.classList.remove('active');

    if (viewName === 'dashboard') {
        viewDashboard.classList.remove('hidden');
        navDashboard.classList.add('active');
        renderApp();
    } else if (viewName === 'compare') {
        viewCompare.classList.remove('hidden');
        if(navCompare) navCompare.classList.add('active');
        chartStartIndex = null; // Reset to focus on current month
        renderCompare();
        
        if (simProjectSelect) {
            simProjectSelect.innerHTML = '<option value="">-- Crear Nuevo / Manual --</option>';
            projects.slice().sort((a, b) => (a.name || '').localeCompare(b.name || '')).forEach(p => {
                const opt = document.createElement('option');
                opt.value = p.id;
                opt.textContent = p.name;
                simProjectSelect.appendChild(opt);
            });
        }
        
        if (simExpenseStartInput && !simExpenseStartInput.value) {
            simExpenseStartInput.value = getMonthKey(currentDate);
        }
        if (simIncomeStartInput && !simIncomeStartInput.value) {
            simIncomeStartInput.value = getMonthKey(currentDate);
        }
    } else if (viewName === 'history') {
        viewHistory.classList.remove('hidden');
        navHistory.classList.add('active');
        renderHistory();
    } else if (viewName === 'workshop') {
        viewWorkshop.classList.remove('hidden');
        navWorkshop.classList.add('active');
        renderWorkshop();
    } else if (viewName === 'archive') {
        if(viewArchive) viewArchive.classList.remove('hidden');
        if(navArchive) navArchive.classList.add('active');
        if(typeof renderArchive === 'function') renderArchive();
    } else if (viewName === 'stats') {
        if(viewStats) viewStats.classList.remove('hidden');
        if(navStats) navStats.classList.add('active');
        populateStatsSelect();
        renderStats();
    } else if (viewName === 'cash') {
        viewCash.classList.remove('hidden');
        navCash.classList.add('active');
        renderCashAdjustment();
    } else if (viewName === 'settings') {
        viewSettings.classList.remove('hidden');
        navSettings.classList.add('active');
    } else if (viewName === 'help') {
        if(viewHelp) viewHelp.classList.remove('hidden');
        if(navHelp) navHelp.classList.add('active');
    }
};

navDashboard.addEventListener('click', () => switchView('dashboard'));
if(navCompare) navCompare.addEventListener('click', () => switchView('compare'));
if(navWorkshop) navWorkshop.addEventListener('click', () => switchView('workshop'));
if(navArchive) navArchive.addEventListener('click', () => switchView('archive'));
if(navStats) navStats.addEventListener('click', () => switchView('stats'));
navHistory.addEventListener('click', () => switchView('history'));
if(navCash) navCash.addEventListener('click', () => switchView('cash'));
navSettings.addEventListener('click', () => switchView('settings'));
if(navHelp) navHelp.addEventListener('click', () => switchView('help'));

// Render History
const renderHistory = () => {
    historyList.innerHTML = '';
    if (expenses.length === 0) {
        historyEmptyState.classList.remove('hidden');
        historyTable.classList.add('hidden');
    } else {
        historyEmptyState.classList.add('hidden');
        historyTable.classList.remove('hidden');
        
        const sortedExpenses = [...expenses].sort((a, b) => {
            const titularCmp = (a.titular || '').localeCompare(b.titular || '');
            if (titularCmp !== 0) return titularCmp;
            
            const cardCmp = (a.card || '').localeCompare(b.card || '');
            if (cardCmp !== 0) return cardCmp;
            
            const getTypeVal = (ex) => ex.is_tax ? 3 : (ex.installmentInfo ? 1 : 2);
            const typeA = getTypeVal(a);
            const typeB = getTypeVal(b);
            if (typeA !== typeB) return typeA - typeB;
            
            return (a.desc || '').localeCompare(b.desc || '');
        });
        
        sortedExpenses.forEach(expense => {
            const tr = document.createElement('tr');
            const cType = getCardTypeByName(expense.card);
            let badgeClass = 'badge-efectivo';
            if (cType === 'visa') badgeClass = 'badge-visa';
            if (cType === 'master') badgeClass = 'badge-mastercard';
            if (cType === 'mercado') badgeClass = 'badge-mercadopago';
            if (cType === 'impuestos') badgeClass = 'badge-impuestos';

            let badgeStyle = '';
            if (cType === 'mercado') badgeStyle = 'style="background-color: #009ee3; color: white; border-color: #009ee3;"';
            if (cType === 'impuestos') badgeStyle = 'style="background-color: #8b5cf6; color: white; border-color: #8b5cf6;"';

            let rowClass = 'row-one-payment';
            if (expense.installmentInfo) rowClass = 'row-installments';
            if (expense.titular === 'Milagros') rowClass = 'row-milagros';
            if (expense.is_tax) rowClass = 'row-tax';
            if (expense.is_adjustment) rowClass = 'row-adjustment';
            
            tr.className = rowClass;

            let projectNameHtml = '';
            if (expense.projectId && expense.projectId !== 'SHARED') {
                const project = projects.find(p => p.id === expense.projectId);
                if (project) {
                    projectNameHtml = `<div style="font-size: 0.8rem; color: var(--accent-primary); margin-top: 0.2rem;"><i class="fa-solid fa-hammer"></i> ${project.name}</div>`;
                }
            } else if (expense.projectId === 'SHARED') {
                const count = expense.sharedProjectIds ? expense.sharedProjectIds.length : 0;
                projectNameHtml = `<div style="font-size: 0.8rem; color: var(--accent-primary); margin-top: 0.2rem;"><i class="fa-solid fa-layer-group"></i> Compartido (${count} proy.)</div>`;
            } else if (expense.projectId === 'TO_ASSIGN') {
                projectNameHtml = `<div style="font-size: 0.8rem; color: #f59e0b; margin-top: 0.2rem;"><i class="fa-solid fa-boxes-stacked"></i> En Inventario</div>`;
            }

            tr.innerHTML = `
                <td>${formatDateDisplay(expense.date)}</td>
                <td><strong>${expense.desc}</strong> <small style="color:var(--text-secondary); margin-left:8px;">${expense.installmentInfo || 'Un pago'}</small>${projectNameHtml}</td>
                <td><span class="badge ${badgeClass}" ${badgeStyle}>${expense.card}</span></td>
                <td>${expense.titular || 'Raúl'}</td>
                <td>${expense.monthKey}</td>
                <td style="font-weight: 600; color: ${expense.amount < 0 ? 'var(--success)' : 'inherit'};">${formatCurrency(expense.amount)}</td>
                <td>
                    <button class="btn-icon" onclick="toggleExpenseSign('${expense.groupId}')" title="Convertir en Devolución/Gasto" style="color: var(--accent-primary); margin-right: 8px;">
                        <i class="fa-solid fa-right-left"></i>
                    </button>
                    <button class="btn-icon" onclick="deleteExpense('${expense.groupId}')" title="Eliminar Gasto">
                        <i class="fa-solid fa-trash"></i>
                    </button>
                </td>
            `;
            historyList.appendChild(tr);
        });
    }
};

// --- STATS LOGIC ---
const populateStatsSelect = () => {
    if (!statsOptgroupActive || !statsOptgroupArchived) return;
    
    const currentVals = Array.from(document.querySelectorAll('.stats-project-cb:checked')).map(cb => cb.value);
    statsOptgroupActive.innerHTML = '';
    statsOptgroupArchived.innerHTML = '';
    
    projects.slice().sort((a, b) => (a.name || '').localeCompare(b.name || '')).forEach(p => {
        const label = document.createElement('label');
        label.style.display = 'flex';
        label.style.justifyContent = 'space-between';
        label.style.alignItems = 'center';
        label.style.padding = '0.4rem 0.5rem';
        label.style.color = '#e2e8f0';
        label.style.cursor = 'pointer';
        label.style.borderRadius = '4px';
        label.innerHTML = `<span>${p.name}</span><input type="checkbox" value="${p.id}" class="stats-project-cb" style="width: 16px; height: 16px; cursor: pointer;">`;
        
        if (p.isArchived) {
            statsOptgroupArchived.appendChild(label);
        } else {
            statsOptgroupActive.appendChild(label);
        }
    });
    
    let hasSelection = false;
    document.querySelectorAll('.stats-project-cb').forEach(cb => {
        if (currentVals.includes(cb.value)) {
            cb.checked = true;
            hasSelection = true;
        } else if (cb.value !== 'all') {
            cb.checked = false;
        }
    });
    
    if (statsMonthsContainer) {
        const currentMonthVals = Array.from(document.querySelectorAll('.stats-month-cb:checked')).map(cb => cb.value);
        statsMonthsContainer.innerHTML = '';
        
        const allMonths = new Set();
        expenses.forEach(ex => allMonths.add(ex.monthKey));
        incomes.forEach(inc => allMonths.add(inc.monthKey));
        projects.forEach(p => { if (p.startDate) allMonths.add(p.startDate.substring(0, 7)); });

        let sortedMonths = Array.from(allMonths).sort().reverse();
        
        // Eliminar meses sin datos
        sortedMonths = sortedMonths.filter(m => {
            const mIncs = getMonthlyIncomes(m).reduce((s, i) => s + i.amount, 0);
            let mExps = 0;
            expenses.forEach(ex => { if (ex.monthKey === m) mExps += ex.amount; });
            return mIncs !== 0 || mExps !== 0 || projects.some(p => p.startDate && p.startDate.startsWith(m));
        });

        sortedMonths.forEach(m => {
            const label = document.createElement('label');
            label.style.display = 'flex';
            label.style.justifyContent = 'space-between';
            label.style.alignItems = 'center';
            label.style.padding = '0.4rem 0.5rem';
            label.style.color = '#e2e8f0';
            label.style.cursor = 'pointer';
            label.style.borderRadius = '4px';
            let [y, mo] = m.split('-');
            label.innerHTML = `<span>${getMonthName(new Date(y, parseInt(mo)-1, 15))}</span><input type="checkbox" value="${m}" class="stats-month-cb" style="width: 16px; height: 16px; cursor: pointer;">`;
            statsMonthsContainer.appendChild(label);
        });

        let hasMonthSelection = false;
        document.querySelectorAll('.stats-month-cb').forEach(cb => {
            if (currentMonthVals.includes(cb.value)) {
                cb.checked = true;
                hasMonthSelection = true;
            } else if (cb.value !== 'all') {
                cb.checked = false;
            }
        });
        
        if (!hasMonthSelection) {
            const allCb = document.querySelector('.stats-month-cb[value="all"]');
            if (allCb) allCb.checked = true;
        }
    }
    
    if (!hasSelection) {
        const allCb = document.querySelector('.stats-project-cb[value="all"]');
        if (allCb) allCb.checked = true;
    }
};

if (statsProjectList) {
    statsProjectList.addEventListener('change', (e) => {
        if (e.target.classList.contains('stats-project-cb')) {
            if (e.target.value === 'all' && e.target.checked) {
                document.querySelectorAll('.stats-project-cb').forEach(cb => {
                    if (cb !== e.target) cb.checked = false;
                });
            } else if (e.target.value !== 'all' && e.target.checked) {
                const allCb = document.querySelector('.stats-project-cb[value="all"]');
                if (allCb) allCb.checked = false;
            }
            
            if (document.querySelectorAll('.stats-project-cb:checked').length === 0) {
                const allCb = document.querySelector('.stats-project-cb[value="all"]');
                if (allCb) allCb.checked = true;
            }
            renderStats();
        }
    });
}
if (statsMonthList) {
    statsMonthList.addEventListener('change', (e) => {
        if (e.target.classList.contains('stats-month-cb')) {
            if (e.target.value === 'all' && e.target.checked) {
                document.querySelectorAll('.stats-month-cb').forEach(cb => {
                    if (cb !== e.target) cb.checked = false;
                });
            } else if (e.target.value !== 'all' && e.target.checked) {
                const allCb = document.querySelector('.stats-month-cb[value="all"]');
                if (allCb) allCb.checked = false;
            }
            
            if (document.querySelectorAll('.stats-month-cb:checked').length === 0) {
                const allCb = document.querySelector('.stats-month-cb[value="all"]');
                if (allCb) allCb.checked = true;
            }
            renderStats();
        }
    });
}

const renderStats = () => {
    const selectedOptions = Array.from(document.querySelectorAll('.stats-project-cb:checked')).map(o => o.value);
    const selectedMonths = document.querySelector('.stats-month-cb') ? Array.from(document.querySelectorAll('.stats-month-cb:checked')).map(o => o.value) : ['all'];
    let totalInc = 0;
    let totalExp = 0;
    let incList = [];
    let expList = [];
    
    const isAll = selectedOptions.includes('all') || selectedOptions.length === 0;
    const isAllMonths = selectedMonths.includes('all') || selectedMonths.length === 0;
    const selectedProjectIds = selectedOptions.filter(v => !v.startsWith('inc_') && !v.startsWith('exp_') && v !== 'all');
    
    const isMonthIncluded = (dateStrOrMonthKey) => {
        if (isAllMonths) return true;
        if (!dateStrOrMonthKey) return true;
        let monthKey;
        if (dateStrOrMonthKey.includes('/')) {
            const parts = dateStrOrMonthKey.split('/');
            if (parts.length === 3) {
                const d = parts[0].padStart(2, '0');
                const m = parts[1].padStart(2, '0');
                const y = parts[2];
                monthKey = `${y}-${m}`;
            } else {
                monthKey = dateStrOrMonthKey;
            }
        } else {
            monthKey = dateStrOrMonthKey.length > 7 ? dateStrOrMonthKey.substring(0, 7) : dateStrOrMonthKey;
        }
        return selectedMonths.includes(monthKey);
    };

    // 1. Incomes
    let targetMonths = [];
    if (isAllMonths) {
        document.querySelectorAll('.stats-month-cb').forEach(cb => {
            if (cb.value !== 'all') targetMonths.push(cb.value);
        });
    } else {
        targetMonths = selectedMonths.filter(m => m !== 'all');
    }

    targetMonths.forEach(mKey => {
        const monthIncomes = getMonthlyIncomes(mKey);
        monthIncomes.forEach(inc => {
            let include = isAll;
            if (!include) {
                if (selectedOptions.includes(`inc_${inc.source}`)) include = true;
                if (inc.projectId && selectedProjectIds.includes(inc.projectId)) include = true;
            }
            
            if (include) {
                totalInc += inc.amount;
                const displayDate = (!inc.appliedFromRecurring && inc.date) ? inc.date : `${mKey}-15`;
                let projName = '';
                if (inc.projectId) {
                    const p = projects.find(proj => proj.id === inc.projectId);
                    if (p) projName = ` [${p.name}]`;
                }
                incList.push({ date: displayDate, desc: inc.desc + projName + (inc.appliedFromRecurring ? ' (Recurrente)' : ''), amount: inc.amount });
            }
        });
    });

    // 2. Expenses
    expenses.forEach(ex => {
        if (!isMonthIncluded(ex.monthKey)) return;
        let include = isAll;
        
        if (!include) {
            const cType = getCardTypeByName(ex.card);
            const isTax = cType === 'impuestos' || ex.is_tax;
            const isCard = !isTax && (cType === 'visa' || cType === 'master' || cType === 'mercado');
            const isCash = !isCard && !isTax;
            
            if (isCard && selectedOptions.includes('exp_cards')) include = true;
            if (isCash && selectedOptions.includes('exp_cash')) include = true;
            if (isTax && selectedOptions.includes('exp_tax')) include = true;
            if (ex.projectId && ex.projectId !== 'SHARED' && ex.projectId !== 'TO_ASSIGN' && selectedProjectIds.includes(ex.projectId)) include = true;
        }
        
        if (include) {
            totalExp += ex.amount;
            let projName = '';
            if (ex.projectId && ex.projectId !== 'SHARED') {
                const p = projects.find(proj => proj.id === ex.projectId);
                if (p) projName = ` [${p.name}]`;
            } else if (ex.projectId === 'SHARED') {
                const count = ex.sharedProjectIds ? ex.sharedProjectIds.length : 0;
                projName = ` [Compartido (${count})]`;
            }
            expList.push({ date: ex.date, desc: ex.desc + projName + (ex.installmentInfo ? ` ${ex.installmentInfo}` : ''), amount: ex.amount });
        } else if (!isAll && ex.projectId === 'SHARED' && ex.sharedProjectIds) {
            const intersectingProjects = ex.sharedProjectIds.filter(id => selectedProjectIds.includes(id));
            if (intersectingProjects.length > 0) {
                const portion = ex.amount / ex.sharedProjectIds.length;
                const totalPortion = portion * intersectingProjects.length;
                totalExp += totalPortion;
                
                const projNames = intersectingProjects.map(id => {
                    const p = projects.find(proj => proj.id === id);
                    return p ? p.name : '';
                }).join(', ');

                expList.push({ date: ex.date, desc: ex.desc + ` [Parte Compartida: ${projNames}]` + (ex.installmentInfo ? ` ${ex.installmentInfo}` : ''), amount: totalPortion });
            }
        }
    });

    // 3. Project specific costs
    if (!isAll) {
        selectedProjectIds.forEach(id => {
            const project = projects.find(p => p.id === id);
            if (project) {
                
                if (project.extraExpenses) {
                    project.extraExpenses.forEach(e => {
                        const amt = parseFloat(e.amount);
                        const itemDate = e.date || project.startDate;
                        if (isMonthIncluded(itemDate)) {
                            expList.push({ date: itemDate, desc: `[${project.name}] ${e.desc}`, amount: amt });
                            totalExp += amt;
                        }
                    });
                }
            }
        });
    }
    
    const balance = totalInc - totalExp;
    
    if (statsTotalIncomes) statsTotalIncomes.textContent = formatCurrency(totalInc);
    if (statsTotalExpenses) statsTotalExpenses.textContent = formatCurrency(totalExp);
    if (statsTotalBalance) {
        statsTotalBalance.textContent = formatCurrency(balance);
        statsTotalBalance.style.color = '#3b82f6';
        statsBalanceCard.style.borderColor = 'rgba(59, 130, 246, 0.3)';
    }
    
    if (statsIncomesList) {
        statsIncomesList.innerHTML = incList.length === 0 ? '<tr><td colspan="3" style="padding: 1rem; text-align: center; color: var(--text-secondary);">No hay ingresos.</td></tr>' : '';
        incList.sort((a, b) => new Date(b.date) - new Date(a.date)).forEach(item => {
            statsIncomesList.innerHTML += `<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding: 0.8rem; color: var(--text-secondary);">${formatDateDisplay(item.date)}</td><td style="padding: 0.8rem;">${item.desc}</td><td style="padding: 0.8rem; text-align: right; color: var(--success); font-weight: 600;">${formatCurrency(item.amount)}</td></tr>`;
        });
    }
    
    if (statsExpensesList) {
        statsExpensesList.innerHTML = expList.length === 0 ? '<tr><td colspan="3" style="padding: 1rem; text-align: center; color: var(--text-secondary);">No hay gastos.</td></tr>' : '';
        expList.sort((a, b) => new Date(b.date) - new Date(a.date)).forEach(item => {
            statsExpensesList.innerHTML += `<tr style="border-bottom: 1px solid rgba(255,255,255,0.05);"><td style="padding: 0.8rem; color: var(--text-secondary);">${formatDateDisplay(item.date)}</td><td style="padding: 0.8rem;">${item.desc}</td><td style="padding: 0.8rem; text-align: right; color: var(--danger); font-weight: 600;">${formatCurrency(item.amount)}</td></tr>`;
        });
    }
};

// --- CASH ADJUSTMENT LOGIC ---
const renderCashAdjustment = () => {
    const currentKey = getMonthKey(currentDate);
    const monthlyExpenses = expenses.filter(ex => ex.monthKey === currentKey);
    const totalExp = monthlyExpenses.reduce((acc, curr) => acc + curr.amount, 0);
    const monthlyIncomes = getMonthlyIncomes(currentKey);
    const sumInc = monthlyIncomes.reduce((acc, curr) => acc + curr.amount, 0);
    const theoreticalBalance = sumInc - totalExp;

    cashTheoreticalBalance.textContent = formatCurrency(theoreticalBalance);
    cashRealInput.value = '';
    cashDiffContainer.classList.add('hidden');
    btnApplyCashAdjustment.disabled = true;
};

const updateCashDifference = () => {
    const currentKey = getMonthKey(currentDate);
    const monthlyExpenses = expenses.filter(ex => ex.monthKey === currentKey);
    const totalExp = monthlyExpenses.reduce((acc, curr) => acc + curr.amount, 0);
    const monthlyIncomes = getMonthlyIncomes(currentKey);
    const sumInc = monthlyIncomes.reduce((acc, curr) => acc + curr.amount, 0);
    const theoreticalBalance = sumInc - totalExp;

    const realCash = parseFloat(cashRealInput.value) || 0;
    const difference = theoreticalBalance - realCash;

    if (cashRealInput.value !== '' && difference > 0.01) {
        cashDiffContainer.classList.remove('hidden');
        cashDifferenceAmount.textContent = formatCurrency(difference);
        btnApplyCashAdjustment.disabled = false;
    } else {
        cashDiffContainer.classList.add('hidden');
        btnApplyCashAdjustment.disabled = true;
    }
};

cashRealInput.addEventListener('input', updateCashDifference);

btnApplyCashAdjustment.addEventListener('click', () => {
    const currentKey = getMonthKey(currentDate);
    const monthlyExpenses = expenses.filter(ex => ex.monthKey === currentKey);
    const totalExp = monthlyExpenses.reduce((acc, curr) => acc + curr.amount, 0);
    const monthlyIncomes = getMonthlyIncomes(currentKey);
    const sumInc = monthlyIncomes.reduce((acc, curr) => acc + curr.amount, 0);
    const theoreticalBalance = sumInc - totalExp;

    const realCash = parseFloat(cashRealInput.value) || 0;
    const difference = theoreticalBalance - realCash;

    if (difference > 0) {
        const now = new Date();
        const dateStr = now.toISOString().split('T')[0];
        const groupId = 'grp_' + Date.now() + Math.random().toString(36).substr(2, 9);

        expenses.push({
            id: 'ex_' + Date.now() + Math.random().toString(36).substr(2, 9),
            groupId: groupId,
            desc: "Ajuste de Efectivo (Varios/Kiosko)",
            amount: difference,
            date: dateStr,
            monthKey: currentKey,
            card: "Efectivo / Débito",
            titular: "Raúl",
            is_tax: false,
            is_adjustment: true,
            installmentInfo: null
        });

        saveExpenses();
        alert(`Ajuste aplicado correctamente. Se ha creado un gasto de ${formatCurrency(difference)}.`);
        switchView('dashboard');
    }
});

if (btnClearCash) {
    btnClearCash.addEventListener('click', renderCashAdjustment);
}

// Settings Handlers
if (btnClearCards) {
    btnClearCards.addEventListener('click', () => {
        if (confirm('¿Estás seguro de borrar todos los gastos de tarjetas (Visa/Mastercard/MercadoPago)?')) {
            expenses = expenses.filter(ex => {
                const cType = getCardTypeByName(ex.card);
                return !(cType === 'visa' || cType === 'master' || cType === 'mercado');
            });
            saveExpenses();
            alert('Gastos de tarjetas borrados.');
        }
    });
}

if (btnClearCashExpenses) {
    btnClearCashExpenses.addEventListener('click', () => {
        if (confirm('¿Estás seguro de borrar todos los gastos en efectivo/débito?')) {
            expenses = expenses.filter(ex => {
                const cType = getCardTypeByName(ex.card);
                return cType === 'visa' || cType === 'master' || cType === 'mercado';
            });
            saveExpenses();
            alert('Gastos en efectivo borrados.');
        }
    });
}

if (btnClearIncomes) {
    btnClearIncomes.addEventListener('click', () => {
        if (confirm('¿Estás seguro de borrar todos los ingresos registrados?')) {
            incomes = [];
            saveIncomes();
            alert('Ingresos borrados.');
        }
    });
}

if (btnClearProjects) {
    btnClearProjects.addEventListener('click', () => {
        if (confirm('¿Estás seguro de borrar todos los proyectos del taller y el archivo?')) {
            projects = [];
            saveProjects();
            alert('Proyectos borrados.');
        }
    });
}

if (btnClearAll) {
    btnClearAll.addEventListener('click', () => {
        if (confirm('⚠️ ADVERTENCIA: ¿Estás completamente seguro de borrar TODOS los datos de la aplicación (gastos, ingresos, proyectos y ajustes)? Esta acción no se puede deshacer.')) {
            expenses = [];
            incomes = [];
            projects = [];
            users = [
                { id: 'u_1', name: 'Raúl', aliases: ['M CIRIGLIANO GEREZ', 'Raúl'] },
                { id: 'u_2', name: 'Milagros', aliases: ['R CIRIGLIANO COYTO', 'Milagros'] }
            ];
            cardsConfig = [
                { id: 'c_visa', name: 'Visa', type: 'visa', aliases: ['Visa'] },
                { id: 'c_master', name: 'Mastercard', type: 'master', aliases: ['Mastercard'] },
                { id: 'c_mp', name: 'Mercado Pago', type: 'mercado', aliases: ['Mercado Pago', 'MercadoPago'] },
                { id: 'c_efec', name: 'Efectivo / Débito', type: 'efectivo', aliases: ['Efectivo', 'Debito', 'Efectivo/Debito'] },
                { id: 'c_tax', name: 'Impuestos y Servicios', type: 'impuestos', aliases: ['Impuestos', 'Servicios'] }
            ];
            workshopConfig = { name: 'Horario Habitual', startTime: '09:00', endTime: '18:00', isActive: true };

            saveExpenses();
            saveIncomes();
            saveProjects();
            saveUsers();
            saveCards();
            localStorage.setItem('balance_workshop_config', JSON.stringify(workshopConfig));
            
            alert('Todos los datos han sido borrados. La página se recargará para aplicar los cambios.');
            window.location.reload();
        }
    });
}

if (btnImportBackupCards) {
    btnImportBackupCards.addEventListener('click', () => {
        importBackupFile.click();
    });
}

if (btnImportBackupCash) {
    btnImportBackupCash.addEventListener('click', () => {
        importBackupFile.click();
    });
}

window.deleteUser = (id) => {
    if (confirm('¿Eliminar este usuario? Sus gastos e ingresos existentes no se borrarán, pero perderán la vinculación directa si vuelves a importar PDFs con su alias.')) {
        users = users.filter(u => u.id !== id);
        saveUsers();
    }
};

window.addUserAlias = (id) => {
    const input = document.getElementById(`new-alias-${id}`);
    const alias = input.value.trim();
    if (alias) {
        const user = users.find(u => u.id === id);
        if (user && !user.aliases.includes(alias)) {
            user.aliases.push(alias);
            saveUsers();
        }
    }
};

if (btnAddUser) {
    btnAddUser.addEventListener('click', () => {
        const name = newUserName.value.trim();
        if (name) {
            users.push({ id: 'u_' + Date.now(), name: name, aliases: [name] });
            newUserName.value = '';
            saveUsers();
        }
    });
}

window.deleteCard = (id) => {
    if (confirm('¿Eliminar esta tarjeta? Sus gastos existentes no se borrarán, pero perderán su asociación exacta.')) {
        cardsConfig = cardsConfig.filter(c => c.id !== id);
        saveCards();
    }
};

window.addCardAlias = (id) => {
    const input = document.getElementById(`new-card-alias-${id}`);
    const alias = input.value.trim();
    if (alias) {
        const card = cardsConfig.find(c => c.id === id);
        if (card) {
            if (!card.aliases) card.aliases = [];
            if (!card.aliases.includes(alias)) {
                card.aliases.push(alias);
                saveCards();
            }
        }
    }
};

if (btnAddCard) {
    btnAddCard.addEventListener('click', () => {
        const name = newCardName.value.trim();
        const type = newCardType.value;
        if (name) {
            cardsConfig.push({ id: 'c_' + Date.now(), name: name, type: type, aliases: [name] });
            newCardName.value = '';
            saveCards();
        }
    });
}

const processImportedData = (importedData, isBackup = false) => {
        try {
            // Caso: Backup de proyectos e inventario
            if (!Array.isArray(importedData) && importedData.type === 'projects_backup') {
                let projectsAdded = 0;
                let expensesAdded = 0;
                
                if (importedData.projects) {
                    importedData.projects.forEach(p => {
                        const exists = projects.find(existing => existing.id === p.id || existing.name === p.name);
                        if (!exists) {
                            projects.push(p);
                            projectsAdded++;
                        }
                    });
                    if (projectsAdded > 0) saveProjects();
                }
                
                if (importedData.expenses) {
                    importedData.expenses.forEach(ex => {
                        const exists = expenses.find(existing => existing.id === ex.id || existing.groupId === ex.groupId);
                        if (!exists) {
                            expenses.push(ex);
                            expensesAdded++;
                        }
                    });
                    if (expensesAdded > 0) saveExpenses();
                }
                
                alert(`¡Éxito! Se importaron ${projectsAdded} proyectos y ${expensesAdded} materiales/gastos de inventario nuevos.`);
                if (projectsAdded > 0 || expensesAdded > 0) {
                    switchView('workshop');
                }
                return;
            }

            // Caso 1: Backup completo
            if (!Array.isArray(importedData) && importedData.expenses && importedData.incomes) {
                if (confirm('Se ha detectado un backup completo. ¿Deseas reemplazar todos tus datos actuales?')) {
                    expenses = importedData.expenses;
                    incomes = importedData.incomes;
                    saveExpenses();
                    saveIncomes();
                    alert("¡Éxito! Backup restaurado.");
                }
                return;
            }

            // Caso 2: Array de gastos (PDF o Backup de Efectivo)
            const importedExpenses = Array.isArray(importedData) ? importedData : null;
            if (!importedExpenses) throw new Error("Formato no reconocido.");
            
            const startMonthStr = getMonthKey(currentDate); 
            
            // Set para registrar gastos que ya han sido emparejados (evita falsos duplicados en compras idénticas)
            const matchedExistingExpenses = new Set();
            
            importedExpenses.forEach(impEx => {
                const totalAmount = impEx.total_amount || impEx.amount;
                const installments = impEx.installments || 1;
                const groupId = impEx.groupId || ('grp_' + Date.now() + Math.random().toString(36).substr(2, 9));
                const amountPerInstallment = totalAmount / installments;
                
                // Si es un backup, respetamos el monthKey que trae. 
                // Si es el JSON del PDF, usamos el mes seleccionado en la app como base.
                let baseYear, baseMonth;
                if (isBackup && impEx.monthKey) {
                    [baseYear, baseMonth] = impEx.monthKey.split('-').map(Number);
                } else {
                    // Calculamos el desfase si el JSON ya trae una proyección
                    // El script de Python genera proyecciones empezando en el mes actual.
                    // Queremos que la primera cuota del JSON caiga en el mes seleccionado.
                    const selectedMonthKey = getMonthKey(currentDate);
                    [baseYear, baseMonth] = selectedMonthKey.split('-').map(Number);
                    
                    if (impEx.monthKey) {
                        // Si el registro importado tiene un mes, calculamos cuántos meses de diferencia hay
                        // respecto al mes "actual" (el que usó el script de Python, que es el mes real de hoy)
                        const now = new Date();
                        const nowKey = getMonthKey(now);
                        const [nowY, nowM] = nowKey.split('-').map(Number);
                        const [impY, impM] = impEx.monthKey.split('-').map(Number);
                        
                        const diffMonths = (impY - nowY) * 12 + (impM - nowM);
                        
                        // Aplicamos ese desfase al mes seleccionado en la app
                        let targetDate = new Date(baseYear, baseMonth - 1 + diffMonths, 1);
                        baseYear = targetDate.getFullYear();
                        baseMonth = targetDate.getMonth() + 1;
                    }
                }
                
                let rawCard = impEx.card || 'Efectivo / Débito';
                let matchedCard = cardsConfig.find(c => c.name.toLowerCase() === rawCard.toLowerCase() || (c.aliases && c.aliases.some(a => a.toLowerCase() === rawCard.toLowerCase())));
                let finalCard = matchedCard ? matchedCard.name : rawCard;

                let rawTitular = impEx.titular || 'Raúl';
                let matchedUser = users.find(u => u.name.toLowerCase() === rawTitular.toLowerCase() || u.aliases.some(a => a.toLowerCase() === rawTitular.toLowerCase()));
                let finalTitular = matchedUser ? matchedUser.name : (rawTitular === 'Titular Principal' ? 'Raúl' : rawTitular);

                for (let i = 1; i <= installments; i++) {
                    const monthKey = `${baseYear}-${String(baseMonth).padStart(2, '0')}`;
                    const targetInst = impEx.installmentInfo || (installments > 1 ? `Cuota ${i}/${installments}` : null);
                    
                    // Buscar si ya existe este mismo gasto (para no duplicar cuotas ni consumos)
                    const existingIdx = expenses.findIndex((ex, idx) => {
                        if (matchedExistingExpenses.has(idx)) return false;
                        if (ex.monthKey !== monthKey) return false;
                        if (ex.card !== finalCard) return false;
                        if (ex.titular !== finalTitular) return false;
                        if (Math.abs(ex.amount - amountPerInstallment) > 0.01) return false;
                        if ((ex.desc || '').trim().toLowerCase() !== (impEx.desc || '').trim().toLowerCase()) return false;
                        
                        if (targetInst) {
                            if (ex.installmentInfo !== targetInst) return false;
                        } else {
                            if (ex.installmentInfo) return false;
                        }
                        
                        return true;
                    });

                    if (existingIdx !== -1) {
                        // Se encontró un gasto idéntico, lo marcamos como emparejado para no contarlo de nuevo
                        matchedExistingExpenses.add(existingIdx);
                    } else {
                        // Es un gasto nuevo, se agrega
                        expenses.push({
                            id: 'ex_' + Date.now() + Math.random().toString(36).substr(2, 9),
                            groupId: groupId,
                            desc: impEx.desc,
                            amount: amountPerInstallment,
                            date: impEx.date || `${baseYear}-${String(baseMonth).padStart(2, '0')}-01`,
                            monthKey: monthKey,
                            card: finalCard,
                            titular: finalTitular,
                            is_tax: impEx.is_tax || false,
                            is_adjustment: impEx.is_adjustment || false,
                            installmentInfo: targetInst
                        });
                        matchedExistingExpenses.add(expenses.length - 1);
                    }

                    baseMonth++;
                    if (baseMonth > 12) {
                        baseMonth = 1;
                        baseYear++;
                    }
                }
            });
            saveExpenses();
            alert(`¡Éxito! Se importaron ${importedExpenses.length} registros.`);
            switchView('dashboard');
        } catch (err) {
            alert("Error al importar: " + err.message);
        }
};

const handleImportFile = (file, isBackup = false) => {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
        try {
            const importedData = JSON.parse(event.target.result);
            processImportedData(importedData, isBackup);
        } catch(e) {
            alert("Error leyendo el archivo JSON: " + e.message);
        }
    };
    reader.readAsText(file);
};

importBackupFile.addEventListener('change', (e) => handleImportFile(e.target.files[0], true));

if (btnImportProjects && importProjectsFile) {
    btnImportProjects.addEventListener('click', () => importProjectsFile.click());
    importProjectsFile.addEventListener('change', (e) => handleImportFile(e.target.files[0], true));
}

// --- INICIO MOTOR DE EXTRACCIÓN DE PDF LOCAL ---
const parseAmountJS = (amountStr) => {
    if (!amountStr) return 0.0;
    amountStr = amountStr.replace(/[-−—–]/g, '-').trim();
    let isNegative = false;
    if (amountStr.endsWith('-') || amountStr.startsWith('-')) {
        isNegative = true;
        amountStr = amountStr.replace(/-/g, '').trim();
    }
    amountStr = amountStr.replace(/\./g, '').replace(',', '.');
    let val = parseFloat(amountStr);
    if (isNaN(val)) return 0.0;
    return isNegative ? -val : val;
};

const isPaymentJS = (descUpper, coupon = "") => {
    const kwList = ["SU PAGO", "PAGO AUTOMATICO", "PAGO ELECTRONICO", "PAGO HOME", "PAGO LINK", "PAGO POR CAJA", "PAGO EN SUCURSAL", "PAGO MIS CUENTAS", "PAGO TARJETA", "PAGO DE RESUMEN", "PAGO BANELCO", "PAGO DE CAJA", "PAGO EN PESOS", "PAGO PESOS", "PAGO DOLARES", "PAGO EN DOLARES", "PAGO CAJERO", "PAGOS LINK"];
    if (kwList.some(kw => descUpper.includes(kw))) return true;
    if (["PAGO", "PAGOS", "SU PAGO"].includes(descUpper.trim())) return true;
    if (coupon === "000000" || coupon === "999999") return true;
    return false;
};

const addMonthsJS = (year, month, delta) => {
    let d = new Date(year, month - 1 + delta, 1);
    return { y: d.getFullYear(), m: d.getMonth() + 1 };
};

const processVisaJS = (lines, usdRate) => {
    const extracted = [];
    let currentTitular = "Raúl";
    const yearNow = new Date().getFullYear();
    const monthNow = new Date().getMonth() + 1;
    
    const dash = "[-−—–]";
    const patternCompra = new RegExp(`^(?:\\s*(\\d{2}\\s+[A-Za-z\\.]+))?\\s*(?<day>\\d{2})\\s+(?<coupon>\\d{6})\\s+(?<desc>.+?)(?:\\s+(?<inst>C\\.\\s*\\d{1,2}\\s*[/-]\\s*\\d{1,2}|\\d{1,2}\\s*[/-]\\s*\\d{1,2}))?\\s*(?:\\(TNA.*?\\))?\\s+(?:(?<currency>U\\$S|US\\$|USD|U\\$|\\$)\\s*)?(?<amount>${dash}?[\\d\\.]+\\,\\d{2}\\s*${dash}?)\\s*$`);
    const patternTax = new RegExp(`^(?:\\s*(\\d{2}\\s+[A-Za-z\\.]+))?\\s*(?<day>\\d{2})\\s+(?<desc>(?:IMPUESTO|INTERESES|IIBB|IVA|DB\\.RG|PERCEP|CARGO|REINTEGRO|DEVOLUCION|BONIF|DESCUENTO|CREDITO|REVERSO|AJUSTE).*?)\\s+(?:(?<currency>U\\$S|US\\$|USD|U\\$|\\$)\\s*)?(?<amount>${dash}?[\\d\\.]+\\,\\d{2}\\s*${dash}?)\\s*$`);
    
    for (let line of lines) {
        if (line.includes("Total Consumos de ")) {
            currentTitular = line.split("Total Consumos de ")[1].replace(/\s+[-−—–]?\s*[\d\.]+\,\d{2}.*/, '').trim();
            continue;
        }
        let matchTax = line.match(patternTax);
        if (matchTax && matchTax.groups) {
            let desc = matchTax.groups.desc.replace("$", "").trim();
            let amount = parseAmountJS(matchTax.groups.amount);
            let descUpper = desc.toUpperCase();
            
            let isUSD = false;
            if (matchTax.groups.currency && matchTax.groups.currency.includes('U')) isUSD = true;
            if (descUpper.includes('US$') || descUpper.includes('U$S') || descUpper.includes('USD')) {
                isUSD = true;
                desc = desc.replace(/U\$S|US\$|USD/ig, '').trim();
            }
            if (isUSD && usdRate) {
                const originalAmount = amount;
                amount = amount * usdRate;
                desc = `${desc} (US$ ${originalAmount.toFixed(2)})`;
            }

            if (amount > 0 && ["REINTEGRO", "DEVOLUCION", "ANULACION", "BONIF", "DESCUENTO", "CREDITO", "REVERSO", "AJUSTE", "SALDO A FAVOR", "DEV ", "REINT "].some(kw => descUpper.includes(kw))) amount = -amount;
            if (isPaymentJS(descUpper)) continue;
            if (amount !== 0) extracted.push({ desc, amount, date: `${yearNow}-${String(monthNow).padStart(2, '0')}-01`, monthKey: `${yearNow}-${String(monthNow).padStart(2, '0')}`, installments: 1, card: "Visa", titular: currentTitular, is_tax: true });
            continue;
        }
        let matchCompra = line.match(patternCompra);
        if (matchCompra && matchCompra.groups) {
            let desc = matchCompra.groups.desc.trim().replace(/^[A-Z\*]\s+/, '');
            let cuotasStr = matchCompra.groups.inst;
            let amount = parseAmountJS(matchCompra.groups.amount);
            let descUpper = desc.toUpperCase();
            
            let isUSD = false;
            if (matchCompra.groups.currency && matchCompra.groups.currency.includes('U')) isUSD = true;
            if (descUpper.includes('US$') || descUpper.includes('U$S') || descUpper.includes('USD')) {
                isUSD = true;
                desc = desc.replace(/U\$S|US\$|USD/ig, '').trim();
            }
            if (isUSD && usdRate) {
                const originalAmount = amount;
                amount = amount * usdRate;
                desc = `${desc} (US$ ${originalAmount.toFixed(2)})`;
            }

            if (amount > 0 && ["REINTEGRO", "DEVOLUCION", "ANULACION", "BONIF", "DESCUENTO", "CREDITO", "REVERSO", "AJUSTE", "SALDO A FAVOR", "DEV ", "REINT "].some(kw => descUpper.includes(kw))) amount = -amount;
            if (isPaymentJS(descUpper, matchCompra.groups.coupon)) continue;
            if (amount === 0) continue;
            
            let currentInst = 1, totalInst = 1, isInstallment = false;
            if (cuotasStr) {
                let cleanInst = cuotasStr.replace(/C\.\s*/g, '');
                let matchInst = cleanInst.match(/(\d+)\s*[/-]\s*(\d+)/);
                if (matchInst) { 
                    currentInst = parseInt(matchInst[1]); 
                    totalInst = parseInt(matchInst[2]); 
                    if (totalInst > 1 && currentInst <= totalInst) {
                        isInstallment = true; 
                    } else {
                        cuotasStr = null;
                    }
                }
            }
            
            const groupId = 'grp_' + Date.now() + Math.random().toString(36).substr(2, 9);

            if (isInstallment) {
                let remaining = totalInst - currentInst;
                for (let i = 0; i <= remaining; i++) {
                    let dObj = addMonthsJS(yearNow, monthNow, i);
                    extracted.push({ desc, amount, date: `${yearNow}-${String(monthNow).padStart(2, '0')}-01`, monthKey: `${dObj.y}-${String(dObj.m).padStart(2, '0')}`, installments: 1, card: "Visa", titular: currentTitular, is_tax: false, installmentInfo: `${currentInst + i}/${totalInst}`, groupId });
                }
            } else {
                extracted.push({ desc, amount, date: `${yearNow}-${String(monthNow).padStart(2, '0')}-01`, monthKey: `${yearNow}-${String(monthNow).padStart(2, '0')}`, installments: 1, card: "Visa", titular: currentTitular, is_tax: false, installmentInfo: cuotasStr || null, groupId });
            }
        }
    }
    return extracted;
};

const processMastercardJS = (lines, usdRate) => {
    const extracted = [];
    let currentTitular = "Raúl";
    const yearNow = new Date().getFullYear();
    const monthNow = new Date().getMonth() + 1;
    
    const dash = "[-−—–]";
    const patternCompra = new RegExp(`^(?<date>\\d{2}-[A-Za-z]{3}-\\d{2})\\s+(?<desc>.+?)(?:\\s+(?<inst>\\d{1,2}\\s*\\/\\s*\\d{1,2}))?(?:\\s+(?<coupon>\\d{4,6}))?\\s+(?:(?<currency>U\\$S|US\\$|USD|U\\$|\\$)\\s*)?(?<amount>${dash}?[\\d\\.]+\\,\\d{2}\\s*${dash}?)\\s*$`);
    const patternTax = new RegExp(`^\\s*(?<desc>(?:INTERESES|IMPUESTO|PERCEP\\.|PERC\\s|IVA|TRANSFER|SALDO PENDIENTE|REINTEGRO|DEVOLUCION|BONIF|DESCUENTO|CREDITO|REVERSO|AJUSTE).*?)\\s+(?:(?<currency>U\\$S|US\\$|USD|U\\$|\\$)\\s*)?(?<amount>${dash}?[\\d\\.]*\\,\\d{2}\\s*${dash}?)(?:\\s+[\\d\\.]*\\,\\d{2})?\\s*$`);
    
    for (let line of lines) {
        let matchTax = line.match(patternTax);
        if (matchTax && matchTax.groups) {
            let desc = matchTax.groups.desc.trim();
            let amount = parseAmountJS(matchTax.groups.amount);
            let descUpper = desc.toUpperCase();
            
            let isUSD = false;
            if (matchTax.groups.currency && matchTax.groups.currency.includes('U')) isUSD = true;
            if (descUpper.includes('US$') || descUpper.includes('U$S') || descUpper.includes('USD')) {
                isUSD = true;
                desc = desc.replace(/U\$S|US\$|USD/ig, '').trim();
            }
            if (isUSD && usdRate) {
                const originalAmount = amount;
                amount = amount * usdRate;
                desc = `${desc} (US$ ${originalAmount.toFixed(2)})`;
            }

            if (amount > 0 && ["REINTEGRO", "DEVOLUCION", "ANULACION", "BONIF", "DESCUENTO", "CREDITO", "REVERSO", "AJUSTE", "SALDO A FAVOR", "DEV ", "REINT "].some(kw => descUpper.includes(kw))) amount = -amount;
            if (isPaymentJS(descUpper)) continue;
            if (amount !== 0) extracted.push({ desc, amount, date: `${yearNow}-${String(monthNow).padStart(2, '0')}-01`, monthKey: `${yearNow}-${String(monthNow).padStart(2, '0')}`, installments: 1, card: "Mastercard", titular: currentTitular, is_tax: true });
            continue;
        }
        
        let matchCompra = line.match(patternCompra);
        if (matchCompra && matchCompra.groups) {
            let desc = matchCompra.groups.desc.trim();
            let cuotasStr = matchCompra.groups.inst;
            let amount = parseAmountJS(matchCompra.groups.amount);
            let descUpper = desc.toUpperCase();
            
            let isUSD = false;
            if (matchCompra.groups.currency && matchCompra.groups.currency.includes('U')) isUSD = true;
            if (descUpper.includes('US$') || descUpper.includes('U$S') || descUpper.includes('USD')) {
                isUSD = true;
                desc = desc.replace(/U\$S|US\$|USD/ig, '').trim();
            }
            if (isUSD && usdRate) {
                const originalAmount = amount;
                amount = amount * usdRate;
                desc = `${desc} (US$ ${originalAmount.toFixed(2)})`;
            }

            if (amount > 0 && ["REINTEGRO", "DEVOLUCION", "ANULACION", "BONIF", "DESCUENTO", "CREDITO", "REVERSO", "AJUSTE", "SALDO A FAVOR", "DEV ", "REINT "].some(kw => descUpper.includes(kw))) amount = -amount;
            if (isPaymentJS(descUpper, matchCompra.groups.coupon)) continue;
            if (amount === 0) continue;
            
            if (desc.includes('PERSFLOW') && cuotasStr) { desc += " " + cuotasStr; cuotasStr = null; }
            
            let currentInst = 1, totalInst = 1, isInstallment = false;
            if (cuotasStr) {
                let matchInst = cuotasStr.match(/(\d+)\s*\/\s*(\d+)/);
                if (matchInst) { 
                    currentInst = parseInt(matchInst[1]); 
                    totalInst = parseInt(matchInst[2]); 
                    if (totalInst > 1 && currentInst <= totalInst) {
                        isInstallment = true; 
                    } else {
                        cuotasStr = null;
                    }
                }
            }
            
            const groupId = 'grp_' + Date.now() + Math.random().toString(36).substr(2, 9);

            if (isInstallment) {
                let remaining = totalInst - currentInst;
                for (let i = 0; i <= remaining; i++) {
                    let dObj = addMonthsJS(yearNow, monthNow, i);
                    extracted.push({ desc, amount, date: `${yearNow}-${String(monthNow).padStart(2, '0')}-01`, monthKey: `${dObj.y}-${String(dObj.m).padStart(2, '0')}`, installments: 1, card: "Mastercard", titular: currentTitular, is_tax: false, installmentInfo: `${currentInst + i}/${totalInst}`, groupId });
                }
            } else {
                extracted.push({ desc, amount, date: `${yearNow}-${String(monthNow).padStart(2, '0')}-01`, monthKey: `${yearNow}-${String(monthNow).padStart(2, '0')}`, installments: 1, card: "Mastercard", titular: currentTitular, is_tax: false, installmentInfo: cuotasStr || null, groupId });
            }
        }
    }
    return extracted;
};

if (btnImportPdf && importPdfFile) {
    btnImportPdf.addEventListener('click', () => importPdfFile.click());
    
    importPdfFile.addEventListener('change', async (e) => {
        const files = Array.from(e.target.files);
        if (files.length === 0) return;
        
        try {
            btnImportPdf.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Procesando PDF(s)...';
            btnImportPdf.disabled = true;
            
            let allExtractedExpenses = [];

            for (const file of files) {
                const arrayBuffer = await file.arrayBuffer();
                const pdf = await pdfjsLib.getDocument({data: arrayBuffer}).promise;
                
                let fullTextLines = [];
                for (let i = 1; i <= pdf.numPages; i++) {
                    const page = await pdf.getPage(i);
                    const textContent = await page.getTextContent();
                    
                    let items = textContent.items.filter(item => item.str.trim() || item.str === " ");
                    items.sort((a, b) => {
                        if (Math.abs(b.transform[5] - a.transform[5]) > 4) {
                            return b.transform[5] - a.transform[5]; // Sort by Y descending
                        }
                        return a.transform[4] - b.transform[4]; // Sort by X ascending
                    });

                    let lastY = -1;
                    let lastX = -1;
                    let lastWidth = 0;
                    let currentLine = "";

                    items.forEach(item => {
                        if (lastY !== -1 && Math.abs(lastY - item.transform[5]) > 4) {
                            fullTextLines.push(currentLine.trim());
                            currentLine = item.str;
                        } else {
                            let spacing = "";
                            if (lastX !== -1) {
                                let distance = item.transform[4] - (lastX + lastWidth);
                                if (distance > 6) spacing = "   ";
                                else if (!currentLine.endsWith(" ") && !item.str.startsWith(" ")) spacing = " ";
                            }
                            currentLine += spacing + item.str;
                        }
                        lastY = item.transform[5];
                        lastX = item.transform[4];
                        lastWidth = item.width || (item.str.length * 4);
                    });
                    if (currentLine) fullTextLines.push(currentLine.trim());
                }
                
                const fullTextStr = fullTextLines.join('\n').toUpperCase();
                let extracted = [];
                
                const currentUsdRate = parseFloat(document.getElementById('usd-exchange-rate').value) || usdRateConfig;
                
                if (fullTextStr.includes('VISA')) {
                    extracted = processVisaJS(fullTextLines, currentUsdRate);
                } else if (fullTextStr.includes('MASTERCARD')) {
                    extracted = processMastercardJS(fullTextLines, currentUsdRate);
                }
                
                if (extracted.length > 0) {
                    allExtractedExpenses = allExtractedExpenses.concat(extracted);
                }
            }

            if (allExtractedExpenses.length > 0) {
                processImportedData(allExtractedExpenses, false); // ¡Reutilizamos tu lógica!
            } else {
                alert("Los archivos se leyeron, pero no se encontraron gastos nuevos o válidos.");
            }
        } catch (err) {
            alert("Hubo un error al leer el PDF: " + err.message);
            console.error(err);
        } finally {
            btnImportPdf.innerHTML = '<i class="fa-solid fa-file-pdf"></i> Procesar PDF (Visa/Master)';
            btnImportPdf.disabled = false;
            importPdfFile.value = ''; // Reset input
        }
    });
}
// --- FIN MOTOR DE EXTRACCIÓN ---

// Month Navigation Handlers
btnPrevMonth.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    chartStartIndex = null;
    renderApp();
});

btnNextMonth.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    chartStartIndex = null;
    renderApp();
});

// Month Picker Logic
const monthPicker = document.getElementById('month-picker');
const btnOpenCalendar = document.getElementById('btn-open-calendar');

if (btnOpenCalendar && monthPicker) {
    const triggerPicker = () => {
        try {
            monthPicker.showPicker();
        } catch (e) {
            monthPicker.click();
        }
    };

    btnOpenCalendar.addEventListener('click', triggerPicker);
    if (currentMonthDisplay) currentMonthDisplay.addEventListener('click', triggerPicker);
    
    monthPicker.addEventListener('change', (e) => {
        if (e.target.value) {
            const [year, month] = e.target.value.split('-').map(Number);
            // Usamos el día 15 para evitar problemas de desfase horario (TZ)
            currentDate = new Date(year, month - 1, 15);
            switchView('dashboard');
            renderApp();
        }
    });
}

// Filter Handlers
if (filterTitular) filterTitular.addEventListener('change', renderApp);
if (filterCard) filterCard.addEventListener('change', renderApp);
if (filterType) filterType.addEventListener('change', renderApp);
if (filterIncomeType) filterIncomeType.addEventListener('change', renderApp);

// Income Modal Functions
if (incomeSource && incomeProjectContainer) {
    incomeSource.addEventListener('change', () => {
        if (incomeSource.value === 'Taller') {
            incomeProjectContainer.style.display = 'block';
        } else {
            incomeProjectContainer.style.display = 'none';
            if (incomeProject) incomeProject.value = '';
        }
    });
}

const openIncomeModal = () => {
    incomeModalOverlay.classList.remove('hidden');
    if (incomeDate) incomeDate.valueAsDate = new Date();
    
    if (incomeProject) {
        incomeProject.innerHTML = '<option value="">-- General (Sin vincular) --</option>';
        projects.slice().sort((a, b) => (a.name || '').localeCompare(b.name || '')).forEach(p => {
            if (!p.isArchived) {
                const opt = document.createElement('option');
                opt.value = p.id;
                opt.textContent = p.name;
                incomeProject.appendChild(opt);
            }
        });
    }
    if (incomeSource) incomeSource.dispatchEvent(new Event('change'));
};

const closeIncomeModal = () => {
    incomeModalOverlay.classList.add('hidden');
    incomeForm.reset();
};

if(btnAddIncome) btnAddIncome.addEventListener('click', openIncomeModal);
if(btnCloseIncomeModal) btnCloseIncomeModal.addEventListener('click', () => { closeIncomeModal(); if (returnToProjectId) { openProjectDetail(returnToProjectId); returnToProjectId = null; } });
if(btnCancelIncome) btnCancelIncome.addEventListener('click', () => { closeIncomeModal(); if (returnToProjectId) { openProjectDetail(returnToProjectId); returnToProjectId = null; } });

// Income Form Submission
if(incomeForm) {
    incomeForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const source = document.getElementById('income-source').value;
        const desc = document.getElementById('income-desc').value;
        const amount = parseFloat(document.getElementById('income-amount').value);
        const isRecurring = document.getElementById('income-recurring').checked;
        const titular = document.getElementById('income-titular') ? document.getElementById('income-titular').value : 'Raúl';
        
        const dateStr = incomeDate ? incomeDate.value : new Date().toISOString().split('T')[0];
        const dateObj = new Date(dateStr + 'T00:00:00');
        const monthKey = getMonthKey(dateObj);
        
        const projId = (incomeProject && incomeProjectContainer.style.display !== 'none') ? incomeProject.value : null;

        incomes.push({
            id: 'inc_' + Date.now() + Math.random().toString(36).substr(2, 9),
            source: source,
            desc: desc,
            titular: titular,
            amount: amount,
            date: dateStr,
            monthKey: monthKey,
            isRecurring: isRecurring,
            projectId: projId
        });

        saveIncomes();
        closeIncomeModal();
        
        currentDate = new Date(`${monthKey}-15T00:00:00`);
        if (returnToProjectId) {
            switchView('workshop');
            openProjectDetail(returnToProjectId);
            returnToProjectId = null;
        } else {
            switchView('dashboard');
        }
    });
}

// Expense Form Submission
expenseForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    let desc = document.getElementById('expense-desc').value;
    let totalAmount = parseFloat(document.getElementById('expense-amount').value);
    const dateStr = document.getElementById('expense-date').value;
    const card = document.getElementById('expense-card').value;
    const titular = document.getElementById('expense-titular').value;
    const installments = parseInt(document.getElementById('expense-installments').value);
    const startMonthStr = document.getElementById('expense-start-month').value; // YYYY-MM
    
    if (expenseIsUsd && expenseIsUsd.checked) {
        const originalAmount = totalAmount;
        totalAmount = totalAmount * usdRateConfig;
        desc = `${desc} (US$ ${originalAmount.toFixed(2)})`;
    }

    const expenseProjectCheckboxes = document.querySelectorAll('.expense-project-cb:checked');
    const selectedOptions = Array.from(expenseProjectCheckboxes).map(cb => cb.value);
    
    let projectId = null;
    let sharedProjectIds = undefined;

    if (selectedOptions.includes("TO_ASSIGN")) {
        projectId = 'TO_ASSIGN';
    } else {
        const validProjects = selectedOptions.filter(v => v !== "");
        if (validProjects.length === 1) {
            projectId = validProjects[0];
        } else if (validProjects.length > 1) {
            projectId = 'SHARED';
            sharedProjectIds = validProjects;
        }
    }

    const groupId = 'grp_' + Date.now() + Math.random().toString(36).substr(2, 9);
    // El usuario ingresa el valor de la cuota (no se divide)
    const amountPerInstallment = totalAmount;
    
    let [year, month] = startMonthStr.split('-').map(Number);

    for (let i = 1; i <= installments; i++) {
        const monthKey = `${year}-${String(month).padStart(2, '0')}`;
        
        expenses.push({
            id: 'ex_' + Date.now() + Math.random().toString(36).substr(2, 9),
            groupId: groupId,
            desc: desc,
            amount: amountPerInstallment,
            date: dateStr, // keep original purchase date for reference
            monthKey: monthKey,
            card: card,
            titular: titular,
            is_tax: false,
            installmentInfo: installments > 1 ? `Cuota ${i}/${installments}` : null,
            projectId: projectId,
            sharedProjectIds: sharedProjectIds
        });

        // Add 1 month mathematically to avoid Date object day-rollover bugs
        month++;
        if (month > 12) {
            month = 1;
            year++;
        }
    }

    saveExpenses();
    closeModal();
    
    // Jump to the month where the expense starts
    currentDate = new Date(`${startMonthStr}-02T00:00:00`);
    if (returnToProjectId) {
        switchView('workshop');
        openProjectDetail(returnToProjectId);
        returnToProjectId = null;
    } else {
        switchView('dashboard');
    }
});

// JSON Export Logic
const downloadJSON = (data, filename) => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data, null, 4));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", filename);
    document.body.appendChild(downloadAnchorNode); 
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
};

if (btnExportCards) {
    btnExportCards.addEventListener('click', () => {
        const filtered = expenses.filter(ex => {
            const cType = getCardTypeByName(ex.card);
            return cType === 'visa' || cType === 'master' || cType === 'mercado';
        });
        const dateStr = new Date().toISOString().split('T')[0];
        downloadJSON(filtered, `gastos_tarjetas_${dateStr}.json`);
    });
}

if (btnExportCash) {
    btnExportCash.addEventListener('click', () => {
        const filtered = expenses.filter(ex => {
            const cType = getCardTypeByName(ex.card);
            return !(cType === 'visa' || cType === 'master' || cType === 'mercado');
        });
        const dateStr = new Date().toISOString().split('T')[0];
        downloadJSON(filtered, `gastos_efectivo_${dateStr}.json`);
    });
}

if (btnExportBackup) {
    btnExportBackup.addEventListener('click', () => {
        const backupData = {
            expenses: expenses,
            incomes: incomes,
            projects: projects,
            workshopConfig: workshopConfig,
            exportDate: new Date().toISOString()
        };
        const dateStr = new Date().toISOString().split('T')[0];
        downloadJSON(backupData, `balance_completo_${dateStr}.json`);
    });
}

if (btnExportProjects) {
    btnExportProjects.addEventListener('click', () => {
        const includeInventory = confirm('¿Deseas incluir también los materiales y gastos del Inventario (Compartidos/Pendientes) en este backup?');
        const backupData = {
            type: 'projects_backup',
            projects: projects,
            exportDate: new Date().toISOString()
        };
        if (includeInventory) {
            backupData.expenses = expenses.filter(ex => ex.projectId === 'TO_ASSIGN' || ex.projectId === 'SHARED');
        }
        const dateStr = new Date().toISOString().split('T')[0];
        downloadJSON(backupData, `backup_proyectos_${dateStr}.json`);
    });
}

if (btnImportFullBackup) {
    btnImportFullBackup.addEventListener('click', () => {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = '.json';
        input.onchange = (e) => {
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = (event) => {
                try {
                    const data = JSON.parse(event.target.result);
                    if (confirm('Esto reemplazará todos tus datos actuales por los del backup. ¿Deseas continuar?')) {
                        if (data.expenses) {
                            expenses = data.expenses;
                            saveExpenses();
                        }
                        if (data.incomes) {
                            incomes = data.incomes;
                            saveIncomes();
                        }
                        if (data.projects) {
                            projects = data.projects;
                            saveProjects();
                        }
                        if (data.workshopConfig) {
                            workshopConfig = data.workshopConfig;
                            localStorage.setItem('balance_workshop_config', JSON.stringify(workshopConfig));
                        }
                        alert('Backup importado con éxito. La página se recargará.');
                        window.location.reload();
                    }
                } catch (err) {
                    alert('Error al leer el archivo de backup.');
                }
            };
            reader.readAsText(file);
        };
        input.click();
    });
}

// Chart Navigation Handlers
if (btnChartPrev) {
    btnChartPrev.addEventListener('click', () => {
        if (chartStartIndex > 0) {
            chartStartIndex--;
            renderCompare();
        }
    });
}

if (btnChartNext) {
    btnChartNext.addEventListener('click', () => {
        // We'll be limited by renderCompare boundary check anyway
        chartStartIndex++;
        renderCompare();
    });
}

if (btnComparePrev) {
    btnComparePrev.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        chartStartIndex = null;
        renderCompare();
    });
}

if (btnCompareNext) {
    btnCompareNext.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        chartStartIndex = null;
        renderCompare();
    });
}
// --- WORKSHOP LOGIC ---
const logActivity = (project, message) => {
    if (!project.history) project.history = [];
    project.history.unshift({
        time: new Date().toLocaleString('es-AR'),
        msg: message
    });
};

const saveProjects = () => {
    localStorage.setItem('balance_projects', JSON.stringify(projects));
};

window.dismissPendingExpense = () => {
    const expenseCheckboxes = document.querySelectorAll('.assign-expense-cb:checked');
    const selectedExpenseIds = Array.from(expenseCheckboxes).map(cb => cb.value);
    
    if (selectedExpenseIds.length === 0) {
        alert("Selecciona al menos un gasto pendiente para quitar de la lista.");
        return;
    }

    if (confirm("¿Deseas archivar estos materiales del inventario? Ya no aparecerán en la lista para asignar, pero se mantendrán intactos en los proyectos que ya los estén utilizando.")) {
        expenses.forEach(ex => {
            if (selectedExpenseIds.includes(ex.groupId)) {
                if (ex.projectId === 'TO_ASSIGN') {
                    ex.projectId = null;
                    delete ex.sharedProjectIds;
                } else if (ex.projectId === 'SHARED') {
                    ex.isArchivedShared = true; // Nuevo flag para archivar de la lista
                }
            }
        });
        
        saveExpenses();
        renderWorkshop();
        renderApp();
    }
};

window.assignExpense = () => {
    const expenseCheckboxes = document.querySelectorAll('.assign-expense-cb:checked');
    const selectedExpenseIds = Array.from(expenseCheckboxes).map(cb => cb.value);
    
    if (selectedExpenseIds.length === 0) {
        alert("Selecciona al menos un gasto pendiente para asignar.");
        return;
    }

    const checkboxes = document.querySelectorAll('.assign-pending-cb:checked');
    const selectedIds = Array.from(checkboxes).map(cb => cb.value);
    
    if (selectedIds.length === 0) {
        alert("Selecciona al menos un proyecto para asignar.");
        return;
    }
    
    expenses.forEach(ex => {
        if (selectedExpenseIds.includes(ex.groupId) && (ex.projectId === 'TO_ASSIGN' || ex.projectId === 'SHARED')) {
            ex.projectId = 'SHARED';
            if (!ex.sharedProjectIds) ex.sharedProjectIds = [];
            // Add new selected projects without removing existing ones
            selectedIds.forEach(id => {
                if (!ex.sharedProjectIds.includes(id)) {
                    ex.sharedProjectIds.push(id);
                }
            });
        }
    });
    
    saveExpenses();
    renderWorkshop();
    renderApp();
};

const renderWorkshop = () => {
    const unassignedExpenseContainer = document.getElementById('unassigned-expense-container');
    const unassignedProjectsContainer = document.getElementById('unassigned-projects-container');
    const workshopUnassignedExpenses = document.getElementById('workshop-unassigned-expenses');
    
    if (unassignedExpenseContainer && unassignedProjectsContainer && workshopUnassignedExpenses) {
        const unassignedGroups = {};
        expenses.forEach(ex => {
            if (ex.projectId === 'TO_ASSIGN' || (ex.projectId === 'SHARED' && !ex.isArchivedShared)) {
                if (!unassignedGroups[ex.groupId]) {
                    unassignedGroups[ex.groupId] = {
                        desc: ex.desc,
                        totalAmount: 0,
                        date: ex.date,
                        groupId: ex.groupId,
                        installmentInfo: ex.installmentInfo ? 'Varias cuotas' : 'Un pago',
                        sharedProjectIds: ex.sharedProjectIds || []
                    };
                }
                unassignedGroups[ex.groupId].totalAmount += ex.amount;
            }
        });

        const groupsArray = Object.values(unassignedGroups);
        
        if (groupsArray.length === 0) {
            workshopUnassignedExpenses.classList.add('hidden');
        } else {
            workshopUnassignedExpenses.classList.remove('hidden');
            
            unassignedExpenseContainer.innerHTML = '';
            groupsArray.sort((a, b) => (a.desc || '').localeCompare(b.desc || '')).forEach(grp => {
                const instText = grp.installmentInfo === 'Varias cuotas' ? ` (Cuotas)` : '';
                const usedText = grp.sharedProjectIds.length > 0 ? ` <span style="color: var(--accent-primary); font-size: 0.8rem; margin-left: 0.5rem;">(${grp.sharedProjectIds.length} proy.)</span>` : '';
                unassignedExpenseContainer.innerHTML += `
                    <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer;">
                        <input type="checkbox" value="${grp.groupId}" class="assign-expense-cb" style="width: 18px; height: 18px;">
                        <span style="font-size: 0.9rem;"><strong>${grp.desc}</strong>${instText}${usedText} <span style="color:var(--text-secondary); margin-left:4px;">- ${formatDateDisplay(grp.date)}</span> <span style="color:var(--danger); margin-left:4px;">| ${formatCurrency(grp.totalAmount)}</span></span>
                    </label>
                `;
            });

            unassignedProjectsContainer.innerHTML = '';
            projects.filter(p => !p.isArchived).sort((a, b) => (a.name || '').localeCompare(b.name || '')).forEach(p => {
                unassignedProjectsContainer.innerHTML += `
                    <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer;">
                        <input type="checkbox" value="${p.id}" class="assign-pending-cb" style="width: 18px; height: 18px;">
                        <span>${p.name}</span>
                    </label>
                `;
            });
        }
    }

    // --- WORKSHOP BALANCE CALCULATOR ---
    if (workshopBalancesContainer && workshopBalanceCalculator) {
        const expectedItemsMap = {};

        projects.forEach(p => {
            if (p.expectedIncomes) {
                p.expectedIncomes.forEach(inc => {
                    const dateStr = inc.date || p.startDate || getMonthKey(currentDate) + '-01';
                    const monthKey = dateStr.substring(0, 7);
                    const key = `${monthKey}|||${p.name}`;
                    
                    if (!expectedItemsMap[key]) {
                        expectedItemsMap[key] = { monthKey, projectName: p.name, amount: 0 };
                    }
                    expectedItemsMap[key].amount += (parseFloat(inc.amount) || 0);
                });
            }
        });

        const sortedItems = Object.values(expectedItemsMap).sort((a, b) => {
            if (a.monthKey !== b.monthKey) return a.monthKey.localeCompare(b.monthKey);
            return a.projectName.localeCompare(b.projectName);
        });
        
        if (sortedItems.length === 0) {
            workshopBalanceCalculator.classList.add('hidden');
        } else {
            workshopBalanceCalculator.classList.remove('hidden');
            workshopBalancesContainer.innerHTML = '';
            
            sortedItems.forEach(item => {
                const bal = item.amount;
                const m = item.monthKey;
                const pName = item.projectName;
                const key = `${m}|||${pName}`;
                
                const chip = document.createElement('label');
                chip.style.display = 'flex';
                chip.style.flexDirection = 'column';
                chip.style.gap = '0.2rem';
                chip.style.padding = '0.6rem 0.8rem';
                chip.style.borderRadius = '12px';
                chip.style.cursor = 'pointer';
                chip.style.border = '1px solid var(--glass-border)';
                chip.style.background = selectedWorkshopMonths.has(key) ? 'rgba(16, 185, 129, 0.2)' : 'rgba(255,255,255,0.05)';
                chip.style.transition = 'all 0.2s';
                chip.style.userSelect = 'none';
                chip.style.minWidth = '160px';
                chip.title = `${pName} (${m})`;
                
                if (selectedWorkshopMonths.has(key)) {
                    chip.style.borderColor = 'rgba(16, 185, 129, 0.5)';
                }
                
                let [y, mo] = m.split('-');
                let d = new Date(y, parseInt(mo)-1, 15);
                const monthName = d.toLocaleDateString('es-AR', { month: 'long', year: 'numeric' });
                
                chip.innerHTML = `
                    <input type="checkbox" value="${key}" class="workshop-month-cb" data-balance="${bal}" data-projects="${pName}" style="display: none;" ${selectedWorkshopMonths.has(key) ? 'checked' : ''}>
                    <div style="display: flex; justify-content: space-between; width: 100%; align-items: center; gap: 0.5rem;">
                        <span style="font-weight: 700; font-size: 0.9rem; color: var(--text-primary); max-width: 140px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${pName}</span>
                        <span style="color: var(--success); font-weight: 800; font-size: 0.9rem;">${formatCurrency(bal)}</span>
                    </div>
                    <span style="font-size: 0.75rem; color: var(--text-secondary); text-transform: capitalize;"><i class="fa-regular fa-calendar"></i> ${monthName}</span>
                `;
                
                chip.querySelector('input').addEventListener('change', (e) => {
                    if (e.target.checked) {
                        selectedWorkshopMonths.add(key);
                        chip.style.background = 'rgba(16, 185, 129, 0.2)';
                        chip.style.borderColor = 'rgba(16, 185, 129, 0.5)';
                    } else {
                        selectedWorkshopMonths.delete(key);
                        chip.style.background = 'rgba(255,255,255,0.05)';
                        chip.style.borderColor = 'var(--glass-border)';
                    }
                    updateWorkshopSelectionSum();
                });
                
                workshopBalancesContainer.appendChild(chip);
            });
            updateWorkshopSelectionSum();
        }
    }

    projectsGrid.innerHTML = '';
    
    const activeProjects = projects.filter(p => !p.isArchived).sort((a, b) => (a.name || '').localeCompare(b.name || ''));
    
    if (activeProjects.length === 0) {
        workshopEmptyState.classList.remove('hidden');
        projectsGrid.classList.add('hidden');
    } else {
        workshopEmptyState.classList.add('hidden');
        projectsGrid.classList.remove('hidden');
        
        activeProjects.forEach(project => {
            const card = document.createElement('div');
            // Use last photo from log if available, otherwise use main image
            const bgImage = (project.photos && project.photos.length > 0) 
                ? project.photos[project.photos.length - 1] 
                : (project.image || 'https://images.unsplash.com/photo-1551218372-a246b7c81784?auto=format&fit=crop&q=80&w=400');
            
            card.className = 'project-card';
            card.setAttribute('draggable', 'true');
            card.dataset.id = project.id;
            card.style.backgroundImage = `url('${bgImage}')`;
            
            // Drag Events
            card.addEventListener('dragstart', handleDragStart);
            card.addEventListener('dragover', handleDragOver);
            card.addEventListener('dragleave', handleDragLeave);
            card.addEventListener('drop', handleDrop);
            card.addEventListener('dragend', handleDragEnd);
            
            // Deadline check
            const today = new Date();
            today.setHours(0,0,0,0);
            const end = project.endDate ? new Date(project.endDate + 'T00:00:00') : null;
            let alarmBorder = '';
            let alarmBadge = '';
            
            if (end && project.status !== 'finalizado') {
                const diffTime = end - today;
                const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
                
                if (diffDays < 0) {
                    alarmBorder = '2px solid #ef4444';
                    alarmBadge = '<span class="badge badge-mastercard" style="position: absolute; top: 10px; right: 10px; background: #ef4444; z-index: 5;">ATRASADO</span>';
                } else if (diffDays <= 2) {
                    alarmBorder = '2px solid #f59e0b';
                    alarmBadge = '<span class="badge badge-mastercard" style="position: absolute; top: 10px; right: 10px; background: #f59e0b; z-index: 5;">PRÓXIMO</span>';
                }
            }
            if (alarmBorder) card.style.border = alarmBorder;

            card.onclick = () => openProjectDetail(project.id);
            
            const completedProcesses = project.processes.filter(p => p.completed).length;
            const progress = project.processes.length > 0 ? (completedProcesses / project.processes.length) * 100 : 0;
            
            let statusColor = 'var(--text-secondary)';
            if (project.status === 'iniciado') statusColor = 'var(--accent-primary)';
            if (project.status === 'finalizado') statusColor = 'var(--success)';
            
            let descriptionSnippet = '';
            if (project.description) {
                descriptionSnippet = `<p style="font-size: 0.8rem; color: var(--text-secondary); margin-top: 0.4rem; line-height: 1.3; overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical;">${project.description}</p>`;
            }

            card.innerHTML = `
                ${alarmBadge}
                <span class="project-status-badge" style="color: ${statusColor}; border: 1px solid ${statusColor}">${project.status.replace('-', ' ')}</span>
                <div class="project-card-content">
                    <h3>${project.name}</h3>
                    ${descriptionSnippet}
                    <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.75rem; opacity: 0.8; margin-top: 0.8rem;">
                        <span><i class="fa-solid fa-calendar"></i> ${formatDateDisplay(project.startDate)}</span>
                        <span>${completedProcesses}/${project.processes.length} pasos</span>
                    </div>
                    <div class="project-progress-container" style="margin-top: 0.8rem; background: rgba(255,255,255,0.2);">
                        <div class="project-progress-bar" style="width: ${progress}%"></div>
                    </div>
                </div>
            `;
            projectsGrid.appendChild(card);
        });
    }
};

const updateWorkshopSelectionSum = () => {
    if (!workshopSelectedSum) return;
    let total = 0;
    const involvedProjects = new Set();
    
    document.querySelectorAll('.workshop-month-cb:checked').forEach(cb => {
        total += parseFloat(cb.dataset.balance);
        if (cb.dataset.projects) {
            cb.dataset.projects.split('|||').forEach(p => {
                if (p) involvedProjects.add(p);
            });
        }
    });
    
    workshopSelectedSum.textContent = formatCurrency(total);
    if (total >= 0) {
        workshopSelectedSum.style.color = '#10b981';
    } else {
        workshopSelectedSum.style.color = '#ef4444';
    }
    
    const descEl = document.getElementById('workshop-selected-projects-desc');
    if (descEl) {
        if (involvedProjects.size > 0) {
            descEl.textContent = `Proyectos seleccionados: ${Array.from(involvedProjects).join(', ')}`;
        } else {
            descEl.textContent = 'Selecciona ítems para ver los proyectos involucrados.';
        }
    }
};

if (btnWorkshopSelectAll) {
    btnWorkshopSelectAll.addEventListener('click', () => {
        document.querySelectorAll('.workshop-month-cb').forEach(cb => {
            if (!cb.checked) {
                cb.checked = true;
                cb.dispatchEvent(new Event('change'));
            }
        });
    });
}

if (btnWorkshopClearAll) {
    btnWorkshopClearAll.addEventListener('click', () => {
        document.querySelectorAll('.workshop-month-cb:checked').forEach(cb => {
            cb.checked = false;
            cb.dispatchEvent(new Event('change'));
        });
    });
}

if (btnRefreshWorkshopCalculator) {
    btnRefreshWorkshopCalculator.addEventListener('click', () => {
        renderWorkshop();
    });
}

const renderArchive = () => {
    if (archiveGrid) {
        archiveGrid.innerHTML = '';
        
        const archivedProjects = projects.filter(p => p.isArchived);
        
        if (archivedProjects.length === 0) {
            if(archiveEmptyState) archiveEmptyState.classList.remove('hidden');
            archiveGrid.classList.add('hidden');
        } else {
            if(archiveEmptyState) archiveEmptyState.classList.add('hidden');
            archiveGrid.classList.remove('hidden');
            
            archivedProjects.sort((a, b) => (a.name || '').localeCompare(b.name || '')).forEach(project => {
                const card = document.createElement('div');
                
                const extrasTotal = (project.extraExpenses || []).reduce((sum, e) => sum + parseFloat(e.amount), 0);
                
                const directExpenses = expenses.filter(ex => ex.projectId === project.id);
                const directExpensesTotal = directExpenses.reduce((sum, ex) => sum + ex.amount, 0);
        
                const sharedExpensesItems = expenses.filter(ex => ex.projectId === 'SHARED' && ex.sharedProjectIds && ex.sharedProjectIds.includes(project.id));
                const sharedExpensesTotal = sharedExpensesItems.reduce((sum, ex) => sum + (ex.sharedProjectIds.length > 0 ? ex.amount / ex.sharedProjectIds.length : 0), 0);
        
                const linkedExpensesTotal = directExpensesTotal + sharedExpensesTotal;
                const totalCost = extrasTotal + linkedExpensesTotal;

                const projectIncomes = incomes.filter(inc => inc.projectId === project.id);
                const totalEarned = projectIncomes.reduce((sum, inc) => sum + inc.amount, 0);
                const balance = totalEarned - totalCost;

                const start = new Date(project.startDate + 'T00:00:00');
                const end = project.endDate ? new Date(project.endDate + 'T00:00:00') : new Date();
                const diffTime = Math.abs(end - start);
                const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
                
                let balanceColor = '#3b82f6';

                card.className = 'project-card glassmorphism';
                card.style.background = 'rgba(0,0,0,0.2)';
                card.style.border = '1px solid var(--glass-border)';
                card.style.cursor = 'pointer';
                card.style.display = 'flex';
                card.style.flexDirection = 'column';
                card.style.padding = '0';
                
                card.onclick = () => openProjectDetail(project.id);
                
                card.innerHTML = `
                    <div style="padding: 1.5rem; flex: 1;">
                        <h3 style="margin-bottom: 0.5rem; color: var(--accent-primary); display: flex; align-items: center; gap: 0.5rem;"><i class="fa-solid fa-box-archive"></i> ${project.name}</h3>
                        <p style="font-size: 0.75rem; color: var(--text-secondary); margin-bottom: 1rem;">${formatDateDisplay(project.startDate)} - ${project.endDate ? formatDateDisplay(project.endDate) : 'Hoy'}</p>
                        
                        <div style="display: flex; flex-direction: column; gap: 0.6rem; font-size: 0.9rem;">
                            <div style="display: flex; justify-content: space-between;">
                                <span style="color: var(--text-secondary);">Duración:</span>
                                <span style="font-weight: 600;">${diffDays} días</span>
                            </div>
                            <div style="display: flex; justify-content: space-between;">
                                <span style="color: var(--text-secondary);">Dinero Gastado:</span>
                                <span style="color: var(--danger); font-weight: 600;">${formatCurrency(totalCost)}</span>
                            </div>
                            <div style="display: flex; justify-content: space-between;">
                                <span style="color: var(--text-secondary);">Dinero Ganado:</span>
                                <span style="color: var(--success); font-weight: 600;">${formatCurrency(totalEarned)}</span>
                            </div>
                        </div>
                    </div>
                    <div style="border-top: 1px solid var(--glass-border); padding: 1rem 1.5rem; background: rgba(0,0,0,0.1); display: flex; justify-content: space-between; font-size: 1.1rem; align-items: center; border-radius: 0 0 12px 12px;">
                        <span style="color: var(--text-secondary); font-size: 0.9rem;">Saldo Final:</span>
                        <span style="color: ${balanceColor}; font-weight: 800;">${formatCurrency(balance)}</span>
                    </div>
                `;
                archiveGrid.appendChild(card);
            });
        }
    }

    const archiveIncomesList = document.getElementById('archive-incomes-list');
    const archiveIncomesEmptyState = document.getElementById('archive-incomes-empty-state');
    const archiveIncomesContainer = document.getElementById('archive-incomes-container');

    if (archiveIncomesList) {
        archiveIncomesList.innerHTML = '';
        const archivedIncomes = incomes.filter(inc => inc.isArchived);

        if (archivedIncomes.length === 0) {
            if(archiveIncomesEmptyState) archiveIncomesEmptyState.classList.remove('hidden');
            if(archiveIncomesContainer) archiveIncomesContainer.classList.add('hidden');
        } else {
            if(archiveIncomesEmptyState) archiveIncomesEmptyState.classList.add('hidden');
            if(archiveIncomesContainer) archiveIncomesContainer.classList.remove('hidden');

            archivedIncomes.sort((a, b) => b.monthKey.localeCompare(a.monthKey)).forEach(inc => {
                const tr = document.createElement('tr');
                tr.style.borderBottom = '1px solid rgba(255,255,255,0.05)';
                
                let totalMonths = 0;
                let sY = 0, sM = 0, eY = 0, eM = 0;
                if(inc.monthKey && inc.endMonthKey) {
                    [sY, sM] = inc.monthKey.split('-').map(Number);
                    [eY, eM] = inc.endMonthKey.split('-').map(Number);
                    totalMonths = (eY - sY) * 12 + (eM - sM) + 1;
                }
                const totalAcumulado = inc.amount * totalMonths;

                let sourceBadge = 'badge-efectivo';
                if (inc.source === 'Escuela') sourceBadge = 'badge-visa';
                if (inc.source === 'Taller') sourceBadge = 'badge-mastercard';

                tr.innerHTML = `
                    <td style="padding: 0.8rem;">
                        <span class="badge ${sourceBadge}" style="margin-right: 0.5rem;">${inc.source}</span>
                        <strong>${inc.desc}</strong>
                    </td>
                    <td style="padding: 0.8rem; color: var(--success); font-weight: 600;">${formatCurrency(inc.amount)}</td>
                    <td style="padding: 0.8rem; color: var(--text-secondary);">${inc.monthKey} a ${inc.endMonthKey} (${totalMonths} meses)</td>
                    <td style="padding: 0.8rem; font-weight: 800; color: var(--accent-primary);">${formatCurrency(totalAcumulado)}</td>
                    <td style="padding: 0.8rem;">
                        <button class="btn-icon" onclick="unarchiveIncome('${inc.id}')" title="Desarchivar" style="color: var(--accent-primary); margin-right: 0.5rem;"><i class="fa-solid fa-box-open"></i></button>
                        <button class="btn-icon" onclick="deleteIncome('${inc.id}')" title="Eliminar" style="color: var(--danger);"><i class="fa-solid fa-trash"></i></button>
                    </td>
                `;
                archiveIncomesList.appendChild(tr);
            });
        }
    }
};

// --- DRAG AND DROP HANDLERS ---
const handleDragStart = (e) => {
    draggedProjectId = e.currentTarget.dataset.id;
    e.currentTarget.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
    // Required for some browsers
    e.dataTransfer.setData('text/plain', draggedProjectId);
};

const handleDragOver = (e) => {
    e.preventDefault(); // Necessary to allow drop
    e.currentTarget.classList.add('drag-over');
    e.dataTransfer.dropEffect = 'move';
};

const handleDragLeave = (e) => {
    e.currentTarget.classList.remove('drag-over');
};

const handleDrop = (e) => {
    e.preventDefault();
    e.currentTarget.classList.remove('drag-over');
    const targetId = e.currentTarget.dataset.id;
    
    if (draggedProjectId === targetId) return;

    const draggedIndex = projects.findIndex(p => p.id === draggedProjectId);
    const targetIndex = projects.findIndex(p => p.id === targetId);

    if (draggedIndex !== -1 && targetIndex !== -1) {
        // Reorder array
        const [draggedProject] = projects.splice(draggedIndex, 1);
        projects.splice(targetIndex, 0, draggedProject);
        
        saveProjects();
        renderWorkshop();
    }
};

const handleDragEnd = (e) => {
    e.currentTarget.classList.remove('dragging');
    // Ensure all cards are cleaned up
    document.querySelectorAll('.project-card').forEach(card => {
        card.classList.remove('drag-over');
    });
};

const openProjectDetail = (projectId) => {
    const project = projects.find(p => p.id === projectId);
    if (!project) return;
    
    if (!project.processes) project.processes = [];
    if (!project.schedules) project.schedules = [];
    
    activeProjectId = projectId;
    detailProjectName.textContent = project.name;
    detailProjectImg.src = project.image || 'https://images.unsplash.com/photo-1551218372-a246b7c81784?auto=format&fit=crop&q=80&w=400';
    detailProjectStatus.textContent = project.status.replace('-', ' ');
    detailProjectStatus.className = `badge badge-${project.status}`;
    
    // Status Tabs
    const tabs = document.querySelectorAll('.status-tab');
    tabs.forEach(tab => {
        tab.classList.remove('active');
        if (tab.dataset.status === project.status) {
            tab.classList.add('active');
        }
        
        // Retomar tab is only visible if current status is finalizado
        if (tab.dataset.status === 'retomar') {
            tab.style.display = (project.status === 'finalizado') ? 'block' : 'none';
        }
    });

    detailProjectDates.textContent = `${formatDateDisplay(project.startDate)} - ${project.endDate ? formatDateDisplay(project.endDate) : 'Sin fecha fin'}`;
    
    if (detailProjectDescription) {
        detailProjectDescription.textContent = project.description || 'Sin descripción';
        detailProjectDescription.style.fontStyle = project.description ? 'normal' : 'italic';
    }
    
    if (btnArchiveProject) {
        if (project.isArchived) {
            btnArchiveProject.innerHTML = '<i class="fa-solid fa-box-open"></i> Desarchivar';
            btnArchiveProject.style.borderColor = 'var(--accent-primary)';
            btnArchiveProject.style.color = 'var(--accent-primary)';
        } else {
            btnArchiveProject.innerHTML = '<i class="fa-solid fa-box-archive"></i> Archivar';
            btnArchiveProject.style.borderColor = 'var(--text-secondary)';
            btnArchiveProject.style.color = 'var(--text-secondary)';
        }
    }
    
    // Alarms
    const today = new Date();
    today.setHours(0,0,0,0);
    const end = project.endDate ? new Date(project.endDate + 'T00:00:00') : null;
    projectDeadlineAlarm.classList.add('hidden');
    
    if (end && project.status !== 'finalizado') {
        const diffDays = Math.ceil((end - today) / (1000 * 60 * 60 * 24));
        if (diffDays < 0) {
            projectDeadlineAlarm.classList.remove('hidden');
            projectDeadlineAlarm.className = 'alarm-banner alarm-danger';
            alarmText.textContent = 'PROYECTO ATRASADO - ' + Math.abs(diffDays) + ' días de demora';
        } else if (diffDays <= 2) {
            projectDeadlineAlarm.classList.remove('hidden');
            projectDeadlineAlarm.className = 'alarm-banner alarm-warning';
            alarmText.textContent = 'PLAZO CERCANO - Vence en ' + diffDays + ' días';
        }
    }

    // Render Cost Report
    const extrasTotal = (project.extraExpenses || []).reduce((sum, e) => sum + parseFloat(e.amount), 0);
    
    const directExpenses = expenses.filter(ex => ex.projectId === project.id);
    const directExpensesTotal = directExpenses.reduce((sum, ex) => sum + ex.amount, 0);

    const sharedExpensesItems = expenses.filter(ex => ex.projectId === 'SHARED' && ex.sharedProjectIds && ex.sharedProjectIds.includes(project.id));
    const sharedExpensesTotal = sharedExpensesItems.reduce((sum, ex) => sum + (ex.sharedProjectIds.length > 0 ? ex.amount / ex.sharedProjectIds.length : 0), 0);
    
    const linkedExpensesTotal = directExpensesTotal + sharedExpensesTotal;
    
    document.getElementById('report-cost-extras').textContent = formatCurrency(extrasTotal);
    
    const reportCostLinked = document.getElementById('report-cost-linked');
    if (reportCostLinked) reportCostLinked.textContent = formatCurrency(linkedExpensesTotal);

    const reportCostTotalPresupuestado = document.getElementById('report-cost-total-presupuestado');
    if (reportCostTotalPresupuestado) reportCostTotalPresupuestado.textContent = formatCurrency(extrasTotal);

    const reportCostTotalReal = document.getElementById('report-cost-total-real');
    if (reportCostTotalReal) reportCostTotalReal.textContent = formatCurrency(linkedExpensesTotal);
    
    // Render Real Incomes
    const projectIncomesList = document.getElementById('project-incomes-list');
    const reportExpectedIncome = document.getElementById('report-expected-income');
    const reportRealIncome = document.getElementById('report-real-income');
    
    if (projectIncomesList) {
        const projectIncomes = incomes.filter(inc => inc.projectId === project.id);
        const totalRealIncome = projectIncomes.reduce((sum, inc) => sum + inc.amount, 0);
        
        const expectedTotal = (project.expectedIncomes || []).reduce((sum, e) => sum + parseFloat(e.amount), 0);
        
        if (reportExpectedIncome) reportExpectedIncome.textContent = formatCurrency(expectedTotal);
        if (reportRealIncome) reportRealIncome.textContent = formatCurrency(totalRealIncome);
        
        const reportRealBalance = document.getElementById('report-real-balance');
        if (reportRealBalance) reportRealBalance.textContent = formatCurrency(totalRealIncome - linkedExpensesTotal);
        
        const reportExpectedBalance = document.getElementById('report-expected-balance');
        if (reportExpectedBalance) reportExpectedBalance.textContent = formatCurrency(expectedTotal - extrasTotal);
        
        projectIncomesList.innerHTML = '';
        if (projectIncomes.length === 0) {
            projectIncomesList.innerHTML = '<tr><td colspan="4" style="padding: 1rem; text-align: center; color: var(--text-secondary);">No hay ingresos reales vinculados a este proyecto.</td></tr>';
        } else {
            projectIncomes.sort((a, b) => {
                const dateA = a.date || `${a.monthKey}-01`;
                const dateB = b.date || `${b.monthKey}-01`;
                return new Date(dateB) - new Date(dateA);
            });
            
            projectIncomes.forEach(inc => {
                const tr = document.createElement('tr');
                tr.style.borderBottom = '1px solid rgba(255,255,255,0.05)';
                const displayDate = inc.date ? formatDateDisplay(inc.date) : inc.monthKey;
                
                let sourceBadge = 'badge-efectivo';
                if (inc.source === 'Escuela') sourceBadge = 'badge-visa';
                if (inc.source === 'Taller') sourceBadge = 'badge-mastercard';

                tr.innerHTML = `
                    <td style="padding: 0.5rem; color: var(--text-secondary);">${displayDate}</td>
                    <td style="padding: 0.5rem;">
                        <div style="display: flex; flex-direction: column; gap: 0.3rem;">
                            <span>${inc.desc}</span>
                            <span class="badge ${sourceBadge}" style="align-self: flex-start; font-size: 0.65rem; padding: 0.1rem 0.4rem;">${inc.source} (Ingreso Real)</span>
                        </div>
                    </td>
                    <td style="padding: 0.5rem; text-align: right; font-weight: 600; color: var(--success);">${formatCurrency(inc.amount)}</td>
                    <td style="padding: 0.5rem; text-align: center;">
                        <button class="btn-icon" onclick="deleteIncome('${inc.id}')" style="color: var(--danger);" title="Eliminar Ingreso"><i class="fa-solid fa-trash"></i></button>
                    </td>
                `;
                projectIncomesList.appendChild(tr);
            });
        }
    }

    // Render Linked Expenses
    const linkedExpensesList = document.getElementById('linked-expenses-list');
    if (linkedExpensesList) {
        linkedExpensesList.innerHTML = '';
        
        let displayLinkedExpenses = [];
        
        directExpenses.forEach(ex => {
            displayLinkedExpenses.push({ ...ex, displayAmount: ex.amount, isShared: false });
        });
        
        sharedExpensesItems.forEach(ex => {
            displayLinkedExpenses.push({ 
                ...ex, 
                displayAmount: ex.amount / ex.sharedProjectIds.length, 
                isShared: true,
                splitCount: ex.sharedProjectIds.length
            });
        });

        if (displayLinkedExpenses.length === 0) {
            linkedExpensesList.innerHTML = '<tr><td colspan="4" style="padding: 1rem; text-align: center; color: var(--text-secondary);">No hay gastos vinculados a este proyecto.</td></tr>';
        } else {
            displayLinkedExpenses.sort((a, b) => a.monthKey.localeCompare(b.monthKey)).forEach(ex => {
                const tr = document.createElement('tr');
                tr.style.borderBottom = '1px solid rgba(255,255,255,0.05)';
                
                const [y, m] = ex.monthKey.split('-');
                const assignMonth = new Date(y, parseInt(m)-1, 15).toLocaleDateString('es-AR', { month: 'short', year: 'numeric' });
                const purchaseDate = ex.date ? formatDateDisplay(ex.date) : '';

                const cType = getCardTypeByName(ex.card);
                let badgeClass = 'badge-efectivo';
                if (cType === 'visa') badgeClass = 'badge-visa';
                if (cType === 'master') badgeClass = 'badge-mastercard';
                if (cType === 'mercado') badgeClass = 'badge-mercadopago';
                if (cType === 'impuestos') badgeClass = 'badge-impuestos';

                let badgeStyle = 'align-self: flex-start; font-size: 0.65rem; padding: 0.1rem 0.4rem;';
                if (cType === 'mercado') badgeStyle += ' background-color: #009ee3; color: white; border-color: #009ee3;';
                if (cType === 'impuestos') badgeStyle += ' background-color: #8b5cf6; color: white; border-color: #8b5cf6;';

                let descInfo = ex.isShared ? `<small style="color:var(--text-secondary); margin-left:5px;">(1/${ex.splitCount} de ${formatCurrency(ex.amount)})</small>` : '';

                tr.innerHTML = `
                    <td style="padding: 0.5rem; color: var(--text-secondary);">
                        <div style="font-weight: 600; text-transform: capitalize; color: var(--text-primary);">${assignMonth}</div>
                        <div style="font-size: 0.65rem; margin-top: 0.2rem;" title="Fecha de compra">C: ${purchaseDate}</div>
                    </td>
                    <td style="padding: 0.5rem;">
                        <div style="display: flex; flex-direction: column; gap: 0.3rem;">
                            <span>${ex.desc} <small style="color:var(--text-secondary); margin-left:5px;">${ex.installmentInfo || ''}</small>${descInfo}</span>
                            <span class="badge ${badgeClass}" style="${badgeStyle}">${ex.card} (${ex.isShared ? 'Compartido' : 'Gasto Real'})</span>
                        </div>
                    </td>
                    <td style="padding: 0.5rem; text-align: right; font-weight: 600; color: var(--danger);">${formatCurrency(ex.displayAmount)}</td>
                    <td style="padding: 0.5rem; text-align: center;">
                        <button class="btn-icon" onclick="unlinkExpense('${ex.groupId}', ${ex.isShared})" style="color: var(--text-secondary);" title="Desvincular Gasto (Todas las cuotas)"><i class="fa-solid fa-link-slash"></i></button>
                    </td>
                `;
                linkedExpensesList.appendChild(tr);
            });
        }
    }

    // Render History
    detailHistoryLog.innerHTML = '';
    if (project.history) {
        project.history.forEach(entry => {
            const div = document.createElement('div');
            div.className = 'history-entry';
            div.innerHTML = `<span>${entry.msg}</span><span class="time">${entry.time}</span>`;
            detailHistoryLog.appendChild(div);
        });
    }

    renderExtraExpenses(project);
    renderSharedExpenses(project);
    renderExpectedIncomes(project);
    renderPhotoGallery(project);
    renderProjectProcesses(project);
    renderProjectSchedules(project);
    
    projectDetailModal.classList.remove('hidden');
};

const renderProjectProcesses = (project) => {
    detailProcessesList.innerHTML = '';
    project.processes.forEach((proc, index) => {
        const li = document.createElement('li');
        li.className = `process-item ${proc.completed ? 'completed' : ''}`;
        
        // Deadline check for stage
        let deadlineAlarm = '';
        if (!proc.completed && proc.deadlineDate) {
            const today = new Date();
            const deadline = new Date(proc.deadlineDate + 'T' + (proc.startTime || '00:00'));
            if (deadline < today) {
                deadlineAlarm = `<span style="color: #ef4444; font-size: 0.7rem; font-weight: 700;"><i class="fa-solid fa-clock-rotate-left"></i> ATRASADO</span>`;
            } else if (deadline - today < 24 * 60 * 60 * 1000) {
                deadlineAlarm = `<span style="color: #f59e0b; font-size: 0.7rem; font-weight: 700;"><i class="fa-solid fa-clock"></i> PRÓXIMO</span>`;
            }
        }

        const daysMap = { 'L': 'Lun', 'M': 'Mar', 'X': 'Mié', 'J': 'Jue', 'V': 'Vie', 'S': 'Sáb', 'D': 'Dom' };
        const selectedDays = proc.days ? proc.days.map(d => daysMap[d]).join(', ') : '';
        const timeRange = (proc.startTime && proc.endTime) ? `${proc.startTime} - ${proc.endTime}` : '';

        let timeInfo = '';
        if (proc.completedAt) {
            timeInfo = `<span style="font-size: 0.7rem; color: var(--text-secondary); display: block; margin-top: 0.2rem;">Completado: ${proc.completedAt}</span>`;
        }

        li.innerHTML = `
            <div style="display: flex; align-items: flex-start; gap: 0.8rem; width: 100%;">
                <input type="checkbox" ${proc.completed ? 'checked' : ''} onchange="toggleProcess(${index})" style="margin-top: 0.3rem;">
                <div style="flex: 1;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: 600;">${proc.name}</span>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            ${deadlineAlarm}
                            <button class="btn-icon" onclick="deleteProcess(${index})" style="color: var(--danger); opacity: 0.5; font-size: 0.7rem;"><i class="fa-solid fa-trash"></i></button>
                        </div>
                    </div>
                    <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.2rem;">
                        ${selectedDays ? `<i class="fa-solid fa-calendar-day"></i> ${selectedDays}` : ''}
                        ${timeRange ? ` | <i class="fa-solid fa-clock"></i> ${timeRange}` : ''}
                        ${proc.deadlineDate && !proc.completed ? ` | <i class="fa-solid fa-hourglass-half"></i> Vence: ${proc.deadlineDate}` : ''}
                    </div>
                    ${timeInfo}
                </div>
            </div>
        `;
        detailProcessesList.appendChild(li);
    });
};

const renderProjectSchedules = (project) => {
    detailSchedulesList.innerHTML = '';
    if (project.schedules.length === 0) {
        detailSchedulesList.innerHTML = '<p style="color: var(--text-secondary); font-size: 0.9rem;">No hay horarios registrados.</p>';
    } else {
        project.schedules.sort((a, b) => new Date(a.date) - new Date(b.date)).forEach(sch => {
            const div = document.createElement('div');
            div.className = 'schedule-item glassmorphism';
            div.style.padding = '0.8rem';
            div.style.marginBottom = '0.5rem';
            div.style.display = 'flex';
            div.style.justifyContent = 'space-between';
            div.style.alignItems = 'center';
            
            div.innerHTML = `
                <div>
                    <div style="font-weight: 700; font-size: 0.9rem;">${sch.name || 'Sesión Especial'}</div>
                    <div style="font-size: 0.8rem; color: var(--text-secondary);">
                        <i class="fa-solid fa-calendar-day"></i> 
                        ${sch.dateEnd && sch.dateEnd !== sch.date ? 
                            `${formatDateDisplay(sch.date)} al ${formatDateDisplay(sch.dateEnd)}` : 
                            formatDateDisplay(sch.date)}
                        | <i class="fa-solid fa-clock"></i> ${sch.startTime} - ${sch.endTime}
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <button class="btn-icon" onclick="exportScheduleToGCal('${sch.id}')" title="Exportar a Google Calendar" style="color: #4285f4;">
                        <i class="fa-brands fa-google"></i>
                    </button>
                    <button class="btn-icon" onclick="deleteSchedule('${sch.id}')" title="Eliminar Horario" style="color: var(--danger);">
                        <i class="fa-solid fa-trash"></i>
                    </button>
                </div>
            `;
            detailSchedulesList.appendChild(div);
        });
    }
};

// --- EXTRA EXPENSES LOGIC ---
const renderExtraExpenses = (project) => {
    extraExpensesList.innerHTML = '';
    if (!project.extraExpenses) project.extraExpenses = [];
    
    project.extraExpenses.forEach((exp, index) => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid rgba(255,255,255,0.05)';
        tr.innerHTML = `
            <td style="padding: 0.5rem;">
                <div style="display: flex; flex-direction: column; gap: 0.3rem;">
                    <span>${exp.desc}</span>
                    <span class="badge" style="align-self: flex-start; font-size: 0.65rem; padding: 0.1rem 0.4rem; background: rgba(255,255,255,0.05); color: #94a3b8; border: 1px solid rgba(255,255,255,0.1);">No en Balance</span>
                </div>
            </td>
            <td style="padding: 0.5rem; text-align: right; font-weight: 600;">${formatCurrency(exp.amount)}</td>
            <td style="padding: 0.5rem; text-align: center;">
                <button class="btn-icon" onclick="deleteExtraExpense(${index})" style="color: var(--danger);"><i class="fa-solid fa-trash"></i></button>
            </td>
        `;
        extraExpensesList.appendChild(tr);
    });
};

btnAddExtraExpense.addEventListener('click', () => {
    const project = projects.find(p => p.id === activeProjectId);
    if (!project) return;
    
    const desc = extraExpenseDesc.value;
    const amount = parseFloat(extraExpenseAmount.value);
    
    if (desc && amount > 0) {
        if (!project.extraExpenses) project.extraExpenses = [];
        project.extraExpenses.push({ desc, amount, date: new Date().toLocaleDateString() });
        
        logActivity(project, `Gasto extra añadido: ${desc} (${formatCurrency(amount)})`);
        saveProjects();
        
        extraExpenseDesc.value = '';
        extraExpenseAmount.value = '';
        
        // Refresh
        openProjectDetail(activeProjectId);
    }
});

window.deleteExtraExpense = (index) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (project && confirm('¿Estás seguro de que deseas eliminar este costo estimado?')) {
        const exp = project.extraExpenses[index];
        logActivity(project, `Gasto extra eliminado: ${exp.desc}`);
        project.extraExpenses.splice(index, 1);
        saveProjects();
        openProjectDetail(activeProjectId);
    }
};

// --- EXPECTED INCOMES LOGIC ---
const renderExpectedIncomes = (project) => {
    if (!expectedIncomesList) return;
    expectedIncomesList.innerHTML = '';
    if (!project.expectedIncomes) project.expectedIncomes = [];
    
    project.expectedIncomes.forEach((inc, index) => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid rgba(255,255,255,0.05)';
        
        const qty = inc.qty || 1;
        const unitPrice = inc.unitPrice || inc.amount;
        
        tr.innerHTML = `
            <td style="padding: 0.5rem;">
                <div style="display: flex; flex-direction: column; gap: 0.3rem;">
                    <span>${inc.desc}</span>
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-top: 0.2rem;">
                        <button class="btn-icon" onclick="updateExpectedIncomeQty(${index}, -1)" style="font-size: 0.7rem; background: rgba(255,255,255,0.1); border-radius: 4px; padding: 2px 8px; border: 1px solid var(--glass-border);"><i class="fa-solid fa-minus"></i></button>
                        <span style="font-size: 0.8rem; font-weight: bold; min-width: 45px; text-align: center;">${qty} unid.</span>
                        <button class="btn-icon" onclick="updateExpectedIncomeQty(${index}, 1)" style="font-size: 0.7rem; background: rgba(255,255,255,0.1); border-radius: 4px; padding: 2px 8px; border: 1px solid var(--glass-border);"><i class="fa-solid fa-plus"></i></button>
                        <span style="font-size: 0.7rem; color: var(--text-secondary); margin-left: 0.5rem;">(${formatCurrency(unitPrice)} c/u)</span>
                    </div>
                </div>
            </td>
            <td style="padding: 0.5rem; text-align: right; font-weight: 600; color: var(--success); vertical-align: middle;">${formatCurrency(inc.amount)}</td>
            <td style="padding: 0.5rem; text-align: center; vertical-align: middle;">
                <button class="btn-icon" onclick="deleteExpectedIncome(${index})" style="color: var(--danger);"><i class="fa-solid fa-trash"></i></button>
            </td>
        `;
        expectedIncomesList.appendChild(tr);
    });
};

window.updateExpectedIncomeQty = (index, delta) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (!project || !project.expectedIncomes[index]) return;
    
    const inc = project.expectedIncomes[index];
    let qty = inc.qty || 1;
    let unitPrice = inc.unitPrice || inc.amount;
    
    qty += delta;
    if (qty < 1) return; // Evita cantidades en 0 o negativas (si querés borrarla usás el cesto de basura)
    
    inc.qty = qty;
    inc.unitPrice = unitPrice;
    inc.amount = qty * unitPrice;
    
    saveProjects();
    openProjectDetail(activeProjectId);
    if (typeof renderWorkshop === 'function') renderWorkshop();
};

if (btnAddExpectedIncome) {
    btnAddExpectedIncome.addEventListener('click', () => {
        const project = projects.find(p => p.id === activeProjectId);
        if (!project) return;
        
        const desc = expectedIncomeDesc.value;
        const unitPrice = parseFloat(expectedIncomeAmount.value);
        const qty = expectedIncomeQty ? parseInt(expectedIncomeQty.value) || 1 : 1;
        
        if (desc && unitPrice > 0 && qty > 0) {
            if (!project.expectedIncomes) project.expectedIncomes = [];
            
            const finalDesc = desc;
            const finalAmount = unitPrice * qty;
            
            const now = new Date();
            const formattedDate = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;
            project.expectedIncomes.push({ desc: finalDesc, amount: finalAmount, unitPrice: unitPrice, qty: qty, date: formattedDate });
            
            logActivity(project, `Ingreso proyectado añadido: ${finalDesc} (${formatCurrency(finalAmount)})`);
            saveProjects();
            
            expectedIncomeDesc.value = '';
            expectedIncomeAmount.value = '';
            if (expectedIncomeQty) expectedIncomeQty.value = '1';
            
            openProjectDetail(activeProjectId);
            renderWorkshop();
        }
    });
}

window.deleteExpectedIncome = (index) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (project && confirm('¿Estás seguro de que deseas eliminar este ingreso proyectado?')) {
        const inc = project.expectedIncomes[index];
        logActivity(project, `Ingreso proyectado eliminado: ${inc.desc}`);
        project.expectedIncomes.splice(index, 1);
        saveProjects();
        openProjectDetail(activeProjectId);
        renderWorkshop();
    }
};

const renderSharedExpenses = (project) => {
    const sharedExpensesList = document.getElementById('shared-expenses-list');
    if (!sharedExpensesList) return;
    
    const sharedGroups = {};
    expenses.forEach(ex => {
        if (ex.projectId === 'SHARED') {
            if (!sharedGroups[ex.groupId]) {
                sharedGroups[ex.groupId] = {
                    desc: ex.desc,
                    totalAmount: 0,
                    sharedProjectIds: ex.sharedProjectIds || [],
                    monthKey: ex.monthKey,
                    installmentInfo: ex.installmentInfo ? 'Varias cuotas' : 'Un pago',
                    groupId: ex.groupId
                };
            }
            sharedGroups[ex.groupId].totalAmount += ex.amount;
        }
    });

    sharedExpensesList.innerHTML = '';
    const groupsArray = Object.values(sharedGroups);
    if (groupsArray.length === 0) {
        sharedExpensesList.innerHTML = '<tr><td colspan="5" style="padding: 1rem; text-align: center; color: var(--text-secondary);">No hay gastos compartidos registrados. Crea un Nuevo Gasto y elige "-- Compartido / Divisible --"</td></tr>';
        return;
    }

    groupsArray.sort((a, b) => b.monthKey.localeCompare(a.monthKey)).forEach(grp => {
        const isLinked = grp.sharedProjectIds.includes(project.id);
        // Si está archivado y NO fue usado por este proyecto, lo ocultamos.
        if (grp.isArchivedShared && !isLinked) return;
        
        const splitCount = grp.sharedProjectIds.length;
        const portion = isLinked && splitCount > 0 ? (grp.totalAmount / splitCount) : 0;
        const portionDisplay = isLinked ? formatCurrency(portion) : '-';

        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid rgba(255,255,255,0.05)';
        
        const [y, m] = grp.monthKey.split('-');
        const displayMonth = new Date(y, parseInt(m)-1, 15).toLocaleDateString('es-AR', { month: 'short', year: '2-digit' });

        tr.innerHTML = `
            <td style="padding: 0.5rem; color: var(--text-secondary); text-transform: capitalize;">${displayMonth}</td>
            <td style="padding: 0.5rem;">${grp.desc} <small style="color:var(--text-secondary); margin-left: 5px;">(${splitCount} proy.)</small></td>
            <td style="padding: 0.5rem; text-align: right; color: var(--danger);">${formatCurrency(grp.totalAmount)}</td>
            <td style="padding: 0.5rem; text-align: right; font-weight: 600; color: ${isLinked ? 'var(--danger)' : 'var(--text-secondary)'};">${portionDisplay}</td>
            <td style="padding: 0.5rem; text-align: center;">
                <input type="checkbox" ${isLinked ? 'checked' : ''} onchange="toggleSharedExpense('${grp.groupId}', this.checked)" style="width: 16px; height: 16px; cursor: pointer;">
            </td>
        `;
        sharedExpensesList.appendChild(tr);
    });
};

window.toggleSharedExpense = (groupId, isChecked) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (!project) return;
    
    expenses.forEach(ex => {
        if (ex.groupId === groupId && ex.projectId === 'SHARED') {
            if (!ex.sharedProjectIds) ex.sharedProjectIds = [];
            if (isChecked && !ex.sharedProjectIds.includes(project.id)) {
                ex.sharedProjectIds.push(project.id);
            } else if (!isChecked && ex.sharedProjectIds.includes(project.id)) {
                ex.sharedProjectIds = ex.sharedProjectIds.filter(id => id !== project.id);
            }
        }
    });
    
    saveExpenses();
    openProjectDetail(project.id);
    if (typeof renderArchive === 'function' && !document.getElementById('view-archive').classList.contains('hidden')) renderArchive();
};

window.unlinkExpense = (groupId, isShared) => {
    if (confirm('¿Desvincular este gasto (y todas sus cuotas) del proyecto? (El gasto seguirá existiendo en tu historial general)')) {
        let changed = false;
        expenses.forEach(e => {
            if (e.groupId === groupId) {
                if (isShared && e.sharedProjectIds && activeProjectId) {
                    e.sharedProjectIds = e.sharedProjectIds.filter(id => id !== activeProjectId);
                    changed = true;
                } else if (!isShared) {
                    e.projectId = null;
                    changed = true;
                }
            }
        });
        if (changed) {
            saveExpenses();
            if (activeProjectId) openProjectDetail(activeProjectId);
            if (typeof renderArchive === 'function' && !document.getElementById('view-archive').classList.contains('hidden')) renderArchive();
        }
    }
};

// --- PHOTO GALLERY LOGIC ---
const resizeImage = (file, maxWidth = 1024, quality = 0.7) => {
    return new Promise((resolve) => {
        const reader = new FileReader();
        reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
                const canvas = document.createElement('canvas');
                let width = img.width;
                let height = img.height;

                if (width > maxWidth) {
                    height = (maxWidth / width) * height;
                    width = maxWidth;
                }

                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, width, height);
                resolve(canvas.toDataURL('image/jpeg', quality));
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    });
};

const renderPhotoGallery = (project) => {
    projectPhotoGallery.innerHTML = '';
    if (!project.photos) project.photos = [];
    
    project.photos.forEach((url, index) => {
        const div = document.createElement('div');
        div.className = 'photo-item';
        div.innerHTML = `
            <img src="${url}" alt="Foto del proyecto" onclick="window.open('${url}', '_blank')">
            <button class="btn-delete-photo" onclick="deletePhoto(${index})"><i class="fa-solid fa-trash"></i></button>
        `;
        projectPhotoGallery.appendChild(div);
    });
};

btnAddPhoto.addEventListener('click', () => {
    const project = projects.find(p => p.id === activeProjectId);
    if (!project) return;
    
    const url = newPhotoUrl.value;
    if (url) {
        if (!project.photos) project.photos = [];
        project.photos.push(url);
        logActivity(project, 'Nueva foto añadida al registro fotográfico');
        saveProjects();
        newPhotoUrl.value = '';
        renderPhotoGallery(project);
    }
});

if (btnTriggerUpload) {
    btnTriggerUpload.addEventListener('click', () => photoFileInput.click());
}

if (photoFileInput) {
    photoFileInput.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        
        const project = projects.find(p => p.id === activeProjectId);
        if (project) {
            const base64 = await resizeImage(file);
            if (!project.photos) project.photos = [];
            project.photos.push(base64);
            logActivity(project, 'Nueva foto subida desde archivo');
            saveProjects();
            renderPhotoGallery(project);
            renderWorkshop(); // Update card bg if needed
            photoFileInput.value = ''; // Reset
        }
    });
}

if (btnUploadProjectImage) {
    btnUploadProjectImage.addEventListener('click', () => projectImageFile.click());
}

if (projectImageFile) {
    projectImageFile.addEventListener('change', async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        
        const base64 = await resizeImage(file);
        document.getElementById('project-image').value = base64;
        projectImageFile.value = ''; // Reset
    });
}

window.deletePhoto = (index) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (project && confirm('¿Eliminar esta foto del registro?')) {
        project.photos.splice(index, 1);
        saveProjects();
        renderPhotoGallery(project);
    }
};

window.toggleProcess = (index) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (project) {
        const proc = project.processes[index];
        proc.completed = !proc.completed;
        proc.completedAt = proc.completed ? new Date().toLocaleString('es-AR') : null;
        
        const action = proc.completed ? 'Completó etapa' : 'Desmarcó etapa';
        logActivity(project, `${action}: ${proc.name}`);
        
        saveProjects();
        renderProjectProcesses(project);
        renderWorkshop();
        // Refresh detail to show log
        openProjectDetail(activeProjectId);
    }
};

window.deleteProcess = (index) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (project && confirm('¿Eliminar esta etapa/objetivo?')) {
        const proc = project.processes[index];
        logActivity(project, `Etapa eliminada: ${proc.name}`);
        project.processes.splice(index, 1);
        saveProjects();
        renderProjectProcesses(project);
        renderWorkshop();
        openProjectDetail(activeProjectId);
    }
};

// Modal Handlers
document.querySelectorAll('.status-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        const project = projects.find(p => p.id === activeProjectId);
        if (!project) return;
        
        const newStatus = tab.dataset.status;
        let logMsg = '';
        
        if (newStatus === 'retomar') {
            project.status = 'iniciado';
            logMsg = 'Proyecto retomado (Estado: Iniciado)';
        } else if (newStatus !== project.status) {
            const oldStatus = project.status;
            project.status = newStatus;
            const statusLabels = { 'en-proyecto': 'En Proyecto', 'iniciado': 'Iniciado', 'finalizado': 'Ejecutando' };
            logMsg = `Estado cambiado de ${statusLabels[oldStatus] || oldStatus} a ${statusLabels[newStatus]}`;
        }
        
        if (logMsg) {
            logActivity(project, logMsg);
            saveProjects();
            openProjectDetail(activeProjectId);
            renderWorkshop();
        }
    });
});

btnAddProject.addEventListener('click', () => {
    activeProjectId = null;
    projectModalTitle.textContent = 'Nuevo Proyecto / Serie';
    projectModalOverlay.classList.remove('hidden');
    document.getElementById('project-start').valueAsDate = new Date();
    document.getElementById('project-description').value = '';
    document.getElementById('project-expected-months').value = '12';
    projectProcessesList.innerHTML = '';
    addProcessInputField(); // Start with one input
});

btnEditProject.addEventListener('click', () => {
    const project = projects.find(p => p.id === activeProjectId);
    if (!project) return;
    
    projectModalTitle.textContent = 'Editar Proyecto';
    document.getElementById('project-name').value = project.name;
    document.getElementById('project-description').value = project.description || '';
    document.getElementById('project-status').value = project.status;
    document.getElementById('project-start').value = project.startDate;
    document.getElementById('project-end').value = project.endDate || '';
    document.getElementById('project-image').value = project.image || '';
    document.getElementById('project-expected-months').value = project.expectedMonths || '12';
    
    projectProcessesList.innerHTML = '';
    projectProcessesList.innerHTML = '';
    projectProcessesList.innerHTML = '';
    project.processes.forEach(proc => addProcessInputField(proc.name, proc.deadlineDate, proc.startTime, proc.endTime, proc.days));
    
    projectDetailModal.classList.add('hidden');
    projectModalOverlay.classList.remove('hidden');
});

const closeProjectModal = () => {
    projectModalOverlay.classList.add('hidden');
    projectForm.reset();
    activeProjectId = null;
};

btnCloseProjectModal.addEventListener('click', closeProjectModal);
btnCancelProject.addEventListener('click', closeProjectModal);

const addProcessInputField = (val = '', date = '', start = '', end = '', selectedDays = []) => {
    const div = document.createElement('div');
    div.className = 'process-input-row';
    div.style.background = 'rgba(255,255,255,0.05)';
    div.style.padding = '1rem';
    div.style.borderRadius = '8px';
    div.style.marginBottom = '1rem';
    div.style.border = '1px solid var(--glass-border)';
    
    const days = ['L', 'M', 'X', 'J', 'V', 'S', 'D'];
    const daysHtml = days.map(d => `
        <label style="margin: 0; cursor: pointer; font-size: 0.75rem; display: flex; flex-direction: column; align-items: center; gap: 0.2rem;">
            <input type="checkbox" class="process-day-checkbox" value="${d}" ${selectedDays.includes(d) ? 'checked' : ''} style="width: 16px; height: 16px;">
            ${d}
        </label>
    `).join('');

    div.innerHTML = `
        <div style="display: flex; gap: 0.5rem; margin-bottom: 0.8rem;">
            <input type="text" placeholder="Nombre de la etapa" class="process-input-name" required style="flex: 2;" value="${val}">
            <button type="button" class="btn-icon" onclick="this.parentElement.parentElement.remove()" style="color: var(--danger);"><i class="fa-solid fa-trash"></i></button>
        </div>
        <div style="display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: 0.8rem; align-items: flex-end;">
            <div class="form-group" style="margin:0">
                <label style="font-size: 0.7rem; margin-bottom: 0.3rem;">Días de trabajo</label>
                <div style="display: flex; gap: 0.6rem;">${daysHtml}</div>
            </div>
            <div class="form-group" style="margin:0">
                <label style="font-size: 0.7rem; margin-bottom: 0.3rem;">De:</label>
                <input type="time" class="process-input-start" value="${start}">
            </div>
            <div class="form-group" style="margin:0">
                <label style="font-size: 0.7rem; margin-bottom: 0.3rem;">A:</label>
                <input type="time" class="process-input-end" value="${end}">
            </div>
        </div>
        <div class="form-group" style="margin: 0.8rem 0 0 0">
            <label style="font-size: 0.7rem; margin-bottom: 0.3rem;">Fecha Límite (Opcional)</label>
            <input type="date" class="process-input-date" value="${date}" style="width: 100%;">
        </div>
    `;
    projectProcessesList.appendChild(div);
};

btnAddProcessStep.addEventListener('click', () => addProcessInputField());

projectForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const name = document.getElementById('project-name').value;
    const description = document.getElementById('project-description').value;
    const status = document.getElementById('project-status').value;
    const startDate = document.getElementById('project-start').value;
    const endDate = document.getElementById('project-end').value;
    const image = document.getElementById('project-image').value;
    
    const expectedMonths = document.getElementById('project-expected-months').value;
    
    const processRows = Array.from(document.querySelectorAll('.process-input-row'));
    
    if (activeProjectId) {
        // Edit Mode
        const project = projects.find(p => p.id === activeProjectId);
        
        // Log changes
        if (project.endDate !== endDate) logActivity(project, `Fecha fin cambiada: ${endDate || 'Sin fecha'}`);
        if (project.status !== status) logActivity(project, `Estado cambiado a: ${status}`);
        
        project.name = name;
        project.description = description;
        project.status = status;
        project.startDate = startDate;
        project.endDate = endDate;
        project.image = image;
        project.expectedMonths = expectedMonths;
        
        // Update processes (preserving completion status if name matches)
        const newProcesses = processRows.map(row => {
            const nameVal = row.querySelector('.process-input-name').value;
            const dateVal = row.querySelector('.process-input-date').value;
            const startVal = row.querySelector('.process-input-start').value;
            const endVal = row.querySelector('.process-input-end').value;
            const daysChecked = Array.from(row.querySelectorAll('.process-day-checkbox:checked')).map(cb => cb.value);
            
            const oldProc = project.processes.find(p => p.name === nameVal);
            return {
                name: nameVal,
                deadlineDate: dateVal,
                startTime: startVal,
                endTime: endVal,
                days: daysChecked,
                completed: oldProc ? oldProc.completed : false,
                completedAt: oldProc ? oldProc.completedAt : null
            };
        });
        project.processes = newProcesses;
        
        logActivity(project, 'Proyecto editado');
    } else {
        // Create Mode
        const processes = processRows.map(row => ({
            name: row.querySelector('.process-input-name').value,
            deadlineDate: row.querySelector('.process-input-date').value,
            startTime: row.querySelector('.process-input-start').value,
            endTime: row.querySelector('.process-input-end').value,
            days: Array.from(row.querySelectorAll('.process-day-checkbox:checked')).map(cb => cb.value),
            completed: false,
            completedAt: null
        }));
        
        const newProject = {
            id: 'proj_' + Date.now() + Math.random().toString(36).substr(2, 9),
            name, description, status, startDate, endDate, image,
            costMaterials: 0, costLabor: 0, hours: 0, hourlyRate: 0, expectedMonths,
            processes,
            schedules: [],
            history: [],
            extraExpenses: [],
            expectedIncomes: [],
            photos: []
        };
        logActivity(newProject, 'Proyecto creado');
        projects.push(newProject);
    }
    
    saveProjects();
    closeProjectModal();
    renderWorkshop();
});

btnCloseDetailModal.addEventListener('click', () => {
    projectDetailModal.classList.add('hidden');
    renderWorkshop(); // Fuerza a recargar la calculadora al cerrar la ventana
});

// Schedule Logic
btnAddSchedule.addEventListener('click', () => {
    addScheduleModal.classList.remove('hidden');
    document.getElementById('schedule-date').valueAsDate = new Date();
});

const closeScheduleModal = () => {
    addScheduleModal.classList.add('hidden');
    scheduleForm.reset();
};

btnCloseScheduleModal.addEventListener('click', closeScheduleModal);
btnCancelSchedule.addEventListener('click', closeScheduleModal);

scheduleForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = scheduleNameInput.value;
    const date = document.getElementById('schedule-date').value;
    const dateEnd = document.getElementById('schedule-date-end').value;
    const startTime = document.getElementById('schedule-start').value;
    const endTime = document.getElementById('schedule-end').value;
    
    const project = projects.find(p => p.id === activeProjectId);
    if (project) {
        project.schedules.push({ id: Date.now(), name, date, dateEnd, startTime, endTime });
        const logMsg = dateEnd && dateEnd !== date ? 
            `Horario especial añadido: ${name} (${date} al ${dateEnd})` : 
            `Horario especial añadido: ${name} (${date})`;
        
        logActivity(project, logMsg);
        saveProjects();
        renderProjectSchedules(project);
        closeScheduleModal();
    }
});

window.exportScheduleToGCal = (scheduleId) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (!project) return;
    const sch = project.schedules.find(s => String(s.id) === String(scheduleId));
    if (!sch) return;

    const text = encodeURIComponent(`Trabajo: ${project.name}`);
    const datePart = sch.date.replace(/-/g, '');
    const startPart = sch.startTime.replace(/:/g, '') + '00';
    const endPart = sch.endTime.replace(/:/g, '') + '00';
    const dates = `${datePart}T${startPart}Z/${datePart}T${endPart}Z`;
    
    const details = encodeURIComponent(`Proyecto: ${project.name}\nHorario de trabajo registrado en BalanceApp.`);
    const gCalUrl = `https://www.google.com/calendar/render?action=TEMPLATE&text=${text}&dates=${dates}&details=${details}`;
    window.open(gCalUrl, '_blank');
};

window.deleteSchedule = (scheduleId) => {
    const project = projects.find(p => p.id === activeProjectId);
    if (project && confirm('¿Eliminar este horario?')) {
        project.schedules = project.schedules.filter(s => String(s.id) !== String(scheduleId));
        saveProjects();
        renderProjectSchedules(project);
    }
};

// Google Calendar Export
btnExportGCal.addEventListener('click', () => {
    const project = projects.find(p => p.id === activeProjectId);
    if (!project) return;
    
    // Create a calendar event for the project end date or current day's work
    const text = encodeURIComponent(`Trabajo: ${project.name}`);
    const dates = project.startDate.replace(/-/g, '') + 'T090000Z/' + (project.endDate || project.startDate).replace(/-/g, '') + 'T180000Z';
    const details = encodeURIComponent(`Proyecto: ${project.name}\nEstado: ${project.status}\nPasos pendientes: ${project.processes.filter(p => !p.completed).map(p => p.name).join(', ')}`);
    
    const gCalUrl = `https://www.google.com/calendar/render?action=TEMPLATE&text=${text}&dates=${dates}&details=${details}`;
    window.open(gCalUrl, '_blank');
});

if (btnSimulateProject) {
    btnSimulateProject.addEventListener('click', () => {
        const project = projects.find(p => p.id === activeProjectId);
        if (!project) return;

        // Solo sumar el presupuesto teórico (Costos Estimados). 
        // Los gastos reales (vinculados) se sumarán dinámicamente mes a mes en el simulador para respetar sus cuotas originales.
        const extrasTotal = (project.extraExpenses || []).reduce((sum, e) => sum + parseFloat(e.amount), 0);

        const totalCost = extrasTotal;

        const expectedTotal = (project.expectedIncomes || []).reduce((sum, e) => sum + parseFloat(e.amount), 0);
        const expMos = parseInt(project.expectedMonths) || 12;

        const startKey = project.startDate ? project.startDate.substring(0, 7) : getMonthKey(currentDate);

        // Añadir a la lista de simulación
        simulatedProjects.push({
            id: 'sim_' + Date.now(),
            projectId: project.id,
            name: project.name,
            cost: totalCost,
            installments: 1,
            expStart: startKey,
            income: parseFloat((expectedTotal / expMos).toFixed(2)),
            incStart: startKey,
            projMonths: expMos
        });
        
        if (typeof renderSimulatedProjects === 'function') {
            renderSimulatedProjects();
        }

        // Cambiar de vista y simular
        projectDetailModal.classList.add('hidden');
        switchView('compare');
        
        setTimeout(() => {
            if (simProjectsList) {
                simProjectsList.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
            runSimulation(false);
        }, 300);
    });
}

if (btnAddMonthlySchedule) {
    btnAddMonthlySchedule.addEventListener('click', () => {
        const project = projects.find(p => p.id === activeProjectId);
        if (!project) return;
        
        if (confirm('¿Deseas agregar un horario diario (9:00 - 18:00) para todos los días del mes actual?')) {
            const now = new Date();
            const year = now.getFullYear();
            const month = now.getMonth();
            const daysInMonth = new Date(year, month + 1, 0).getDate();
            
            for (let d = 1; d <= daysInMonth; d++) {
                const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(d).padStart(2, '0')}`;
                // Check if already exists
                if (!project.schedules.some(s => s.date === dateStr)) {
                    project.schedules.push({
                        id: Date.now() + d,
                        date: dateStr,
                        startTime: "09:00",
                        endTime: "18:00"
                    });
                }
            }
            saveProjects();
            renderProjectSchedules(project);
        }
    });
}

if (btnArchiveProject) {
    btnArchiveProject.addEventListener('click', () => {
        const project = projects.find(p => p.id === activeProjectId);
        if (!project) return;
        
        project.isArchived = !project.isArchived;
        logActivity(project, project.isArchived ? 'Proyecto archivado' : 'Proyecto desarchivado');
        saveProjects();
        
        projectDetailModal.classList.add('hidden');
        if (project.isArchived) {
            switchView('archive');
        } else {
            switchView('workshop');
        }
    });
}

if (btnDeleteProject) {
    btnDeleteProject.addEventListener('click', () => {
        if (confirm('¿Estás seguro de eliminar este proyecto por completo?')) {
            const project = projects.find(p => p.id === activeProjectId);
            const wasArchived = project ? project.isArchived : false;
            projects = projects.filter(p => p.id !== activeProjectId);
            saveProjects();
            projectDetailModal.classList.add('hidden');
            if (wasArchived) {
                if (typeof renderArchive === 'function') renderArchive();
            } else {
                renderWorkshop();
            }
        }
    });
}

// --- WORKSHOP CONFIG LOGIC ---
const saveWorkshopConfig = () => {
    localStorage.setItem('balance_workshop_config', JSON.stringify(workshopConfig));
    renderWorkshopStatus();
};

const renderWorkshopStatus = () => {
    // 1. Dashboard Card
    if (workshopStatusCard) {
        if (workshopConfig.isActive) {
            workshopStatusLabel.textContent = workshopConfig.name || 'Taller: Activo';
            workshopStatusLabel.style.color = 'var(--text-primary)';
            workshopStatusTime.textContent = `${workshopConfig.startTime} - ${workshopConfig.endTime}`;
            workshopStatusTime.style.color = 'var(--accent-primary)';
            workshopStatusIcon.style.color = 'var(--accent-primary)';
            workshopStatusCard.style.border = '1px solid var(--accent-primary)';
            workshopStatusCard.style.boxShadow = '0 8px 32px 0 rgba(79, 70, 229, 0.15)';
        } else {
            workshopStatusLabel.textContent = 'Taller: Vacaciones';
            workshopStatusLabel.style.color = 'var(--text-secondary)';
            workshopStatusTime.textContent = 'Cerrado';
            workshopStatusTime.style.color = 'var(--text-secondary)';
            workshopStatusIcon.style.color = 'var(--text-secondary)';
            workshopStatusCard.style.border = '1px solid var(--text-secondary)';
            workshopStatusCard.style.boxShadow = 'none';
        }
    }

    // 2. Workshop View Widget
    if (workshopStatusWidget) {
        if (workshopConfig.isActive) {
            workshopWidgetLabel.textContent = workshopConfig.name || 'Taller: Activo';
            workshopWidgetTime.textContent = `${workshopConfig.startTime} - ${workshopConfig.endTime}`;
            workshopWidgetTime.style.color = 'var(--accent-primary)';
            workshopWidgetIcon.style.color = 'var(--accent-primary)';
            workshopStatusWidget.style.borderColor = 'var(--accent-primary)';
        } else {
            workshopWidgetLabel.textContent = 'Taller: Vacaciones';
            workshopWidgetTime.textContent = 'Cerrado';
            workshopWidgetTime.style.color = 'var(--text-secondary)';
            workshopWidgetIcon.style.color = 'var(--text-secondary)';
            workshopStatusWidget.style.borderColor = 'var(--glass-border)';
        }
    }
};

const openWorkshopConfig = () => {
    workshopNameInput.value = workshopConfig.name || '';
    workshopIsActiveSelect.value = workshopConfig.isActive.toString();
    workshopStartInput.value = workshopConfig.startTime;
    workshopEndInput.value = workshopConfig.endTime;
    editWorkshopModal.classList.remove('hidden');
};

if(workshopStatusCard) workshopStatusCard.addEventListener('click', openWorkshopConfig);
if(workshopStatusWidget) workshopStatusWidget.addEventListener('click', openWorkshopConfig);

const closeWorkshopConfigModal = () => {
    editWorkshopModal.classList.add('hidden');
};

closeWorkshopModal.addEventListener('click', closeWorkshopConfigModal);
btnCancelWorkshopConfig.addEventListener('click', closeWorkshopConfigModal);

workshopConfigForm.addEventListener('submit', (e) => {
    e.preventDefault();
    workshopConfig.name = workshopNameInput.value || 'Horario Habitual';
    workshopConfig.isActive = workshopIsActiveSelect.value === 'true';
    workshopConfig.startTime = workshopStartInput.value;
    workshopConfig.endTime = workshopEndInput.value;
    
    saveWorkshopConfig();
    closeWorkshopConfigModal();
});

window.addEventListener('resize', () => {
    if (viewCompare && !viewCompare.classList.contains('hidden')) {
        renderCompare();
    }
});

// Init
populateTitularSelects();
populateCardSelects();
renderUsersSettings();
renderCardsSettings();
renderApp();
renderWorkshop();
renderWorkshopStatus();
