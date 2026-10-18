# -*- coding: utf-8 -*-
"""
Dr. Hanane Kashi - Aesthetic Medical Clinic CRM & Admin Dashboard
Tailored for cosmetic doctors, aesthetic clinics, and medical appointment management.
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CLINIC_DIR = Path(__file__).resolve().parent

ADMIN_HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>CRM Médical & Secrétariat | Dr. Hanane Kashi</title>
    <link rel="shortcut icon" href="assets/img/dr-kashi-logo.jpg" type="image/x-icon">

    <!-- CSS -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />
    <link href="assets/css/font-awesome.min.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg-dark: #091310;
            --card-dark: #0f231d;
            --card-border: rgba(197, 160, 89, 0.22);
            --emerald: #0f4c3a;
            --emerald-light: #166534;
            --gold: #c5a059;
            --gold-light: #e5c787;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: 'Plus Jakarta Sans', sans-serif;
            min-height: 100vh;
            margin: 0;
            padding: 0;
        }

        .font-serif {
            font-family: 'Playfair Display', serif;
        }

        /* Top Navigation */
        .admin-nav {
            background: rgba(15, 35, 29, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--card-border);
            padding: 14px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .admin-brand {
            display: flex;
            align-items: center;
            gap: 14px;
            text-decoration: none;
            color: #fff;
        }

        .admin-brand img {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: 2px solid var(--gold);
            object-fit: cover;
        }

        /* KPI Cards */
        .kpi-card {
            background: var(--card-dark);
            border: 1px solid var(--card-border);
            border-radius: 18px;
            padding: 22px 20px;
            transition: all 0.25s ease;
            position: relative;
            overflow: hidden;
        }

        .kpi-card:hover {
            transform: translateY(-3px);
            border-color: var(--gold);
            box-shadow: 0 12px 30px rgba(0,0,0,0.3);
        }

        .kpi-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            margin-bottom: 12px;
        }

        .kpi-val {
            font-size: 30px;
            font-weight: 800;
            color: #fff;
            line-height: 1.1;
        }

        .kpi-label {
            font-size: 13px;
            color: var(--text-muted);
            margin-top: 4px;
            font-weight: 500;
        }

        /* Split Screen Workspace */
        .crm-container {
            padding: 24px;
            max-width: 1540px;
            margin: 0 auto;
        }

        .panel-box {
            background: var(--card-dark);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            padding: 24px;
            height: calc(100vh - 270px);
            min-height: 600px;
            display: flex;
            flex-direction: column;
        }

        .panel-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }

        /* Patient List Table */
        .patient-table-wrap {
            overflow-y: auto;
            flex: 1;
        }

        .patient-row {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 14px;
            padding: 14px 16px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .patient-row:hover, .patient-row.selected {
            background: rgba(197, 160, 89, 0.12);
            border-color: var(--gold);
        }

        .patient-badge {
            font-size: 11px;
            font-weight: 700;
            padding: 5px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .badge-new { background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid #3b82f6; }
        .badge-contacted { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid #f59e0b; }
        .badge-confirmed { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid #10b981; }
        .badge-done { background: rgba(139, 92, 246, 0.2); color: #a78bfa; border: 1px solid #8b5cf6; }
        .badge-cancelled { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid #ef4444; }

        /* Patient Drawer & WhatsApp Generator */
        .patient-detail-box {
            overflow-y: auto;
            flex: 1;
        }

        .template-btn {
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.12);
            color: #fff;
            padding: 12px 14px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 600;
            text-align: left;
            width: 100%;
            margin-bottom: 10px;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .template-btn:hover {
            background: rgba(37, 211, 102, 0.18);
            border-color: #25D366;
            color: #fff;
        }

        .btn-wa-direct {
            background: #25D366;
            color: #fff !important;
            font-weight: 700;
            border-radius: 12px;
            padding: 14px 20px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            text-decoration: none;
            transition: all 0.2s ease;
            border: none;
            font-size: 15px;
            box-shadow: 0 8px 25px rgba(37, 211, 102, 0.3);
        }

        .btn-wa-direct:hover {
            background: #20ba5a;
            transform: translateY(-2px);
            color: #fff;
        }

        /* Filter Tabs */
        .filter-tab {
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 13px;
            font-weight: 600;
            padding: 6px 14px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .filter-tab.active, .filter-tab:hover {
            background: rgba(197, 160, 89, 0.2);
            color: var(--gold);
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--gold); }
    </style>
</head>

<body>

    <!-- Top Navigation -->
    <header class="admin-nav">
        <a href="index.html" class="admin-brand">
            <img src="assets/img/dr-kashi-logo.jpg" alt="Logo">
            <div>
                <h6 class="mb-0 font-serif font-weight-bold" style="color: var(--gold-light); font-size: 18px;">Dr. Hanane Kashi</h6>
                <small class="text-muted">Espace Secrétariat & CRM Médical • Casablanca</small>
            </div>
        </a>

        <div class="d-flex align-items-center gap-3">
            <span class="badge px-3 py-2" style="background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid #10b981; border-radius: 20px;">
                <i class="fa fa-circle mr-1" style="font-size: 8px;"></i> Cabinet Ouvert
            </span>
            <a href="index.html" class="btn btn-outline-light btn-sm font-weight-bold ml-2" style="border-radius: 20px; padding: 6px 16px;">
                <i class="fa fa-external-link mr-1"></i> Voir le Site
            </a>
            <button class="btn btn-sm btn-gold ml-2" onclick="openNewPatientModal()" style="border-radius: 20px;">
                <i class="fa fa-plus mr-1"></i> Nouveau RDV
            </button>
        </div>
    </header>

    <div class="crm-container">
        <!-- KPI Row -->
        <div class="row mb-4">
            <div class="col-lg-3 col-md-6 mb-3 mb-lg-0">
                <div class="kpi-card">
                    <div class="kpi-icon" style="background: rgba(59, 130, 246, 0.15); color: #60a5fa;">
                        <i class="fa fa-calendar-check-o"></i>
                    </div>
                    <div class="kpi-val" id="kpi-total">52</div>
                    <div class="kpi-label">Demandes de Consultation (Ce Mois)</div>
                </div>
            </div>

            <div class="col-lg-3 col-md-6 mb-3 mb-lg-0">
                <div class="kpi-card">
                    <div class="kpi-icon" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24;">
                        <i class="fa fa-whatsapp"></i>
                    </div>
                    <div class="kpi-val" id="kpi-pending">8</div>
                    <div class="kpi-label">En Attente de Confirmation WhatsApp</div>
                </div>
            </div>

            <div class="col-lg-3 col-md-6 mb-3 mb-lg-0">
                <div class="kpi-card">
                    <div class="kpi-icon" style="background: rgba(16, 185, 129, 0.15); color: #34d399;">
                        <i class="fa fa-check-circle-o"></i>
                    </div>
                    <div class="kpi-val" id="kpi-confirmed">38</div>
                    <div class="kpi-label">Consultations Confirmées (73%)</div>
                </div>
            </div>

            <div class="col-lg-3 col-md-6">
                <div class="kpi-card">
                    <div class="kpi-icon" style="background: rgba(197, 160, 89, 0.15); color: var(--gold);">
                        <i class="fa fa-heartbeat"></i>
                    </div>
                    <div class="kpi-val" id="kpi-revenue">94 500 DH</div>
                    <div class="kpi-label">Chiffre d'Affaires Actes Estimé</div>
                </div>
            </div>
        </div>

        <!-- Main Workspace (Split-Screen) -->
        <div class="row">
            <!-- Left Column: Patient Queue -->
            <div class="col-lg-7 mb-4 mb-lg-0">
                <div class="panel-box">
                    <div class="panel-header">
                        <div>
                            <h5 class="font-serif font-weight-bold mb-1 text-white">File d'Attente des Patientes</h5>
                            <small class="text-muted">Cliquez sur une patiente pour charger son dossier et générer son message</small>
                        </div>
                        <button class="btn btn-sm btn-outline-secondary" onclick="exportToCsv()" style="border-radius: 8px; color: var(--text-muted); font-size: 12px;">
                            <i class="fa fa-download mr-1"></i> Export CSV
                        </button>
                    </div>

                    <!-- Multi-factor Filter Bar & Search -->
                    <div class="p-3 mb-3 rounded-lg" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);">
                        <!-- Status Tabs -->
                        <div class="d-flex flex-wrap align-items-center justify-content-between mb-2 pb-2 border-bottom border-secondary" style="border-color: rgba(255,255,255,0.08) !important;">
                            <div class="d-flex flex-wrap gap-1" id="filterTabs">
                                <button class="filter-tab active" onclick="setFilter('all')">Tous (<span id="count-all">0</span>)</button>
                                <button class="filter-tab" onclick="setFilter('Nouveau')">Nouveaux (<span id="count-new">0</span>)</button>
                                <button class="filter-tab" onclick="setFilter('Contacté')">Contactés (<span id="count-contacted">0</span>)</button>
                                <button class="filter-tab" onclick="setFilter('Confirmé')">Confirmés (<span id="count-confirmed">0</span>)</button>
                                <button class="filter-tab" onclick="setFilter('Réalisé')">Réalisés (<span id="count-done">0</span>)</button>
                            </div>
                            <span class="badge badge-dark text-muted" id="filterResultsCount" style="background: rgba(0,0,0,0.4); font-size: 11px;">0 résultat(s)</span>
                        </div>

                        <!-- Dropdowns: Treatment, Date, Source + Live Search -->
                        <div class="row align-items-center">
                            <div class="col-md-4 mb-2 mb-md-0">
                                <select id="filterTreatment" onchange="renderPatients()" class="form-control form-control-sm" style="background: #091310; color: #fff; border: 1px solid rgba(197, 160, 89, 0.4); border-radius: 8px; font-size: 12px;">
                                    <option value="all">🩺 Tous les Actes</option>
                                    <option value="Vallée des Larmes">Vallée des Larmes</option>
                                    <option value="Pommettes">Pommettes</option>
                                    <option value="Jawline">Jawline Texas</option>
                                    <option value="Lèvres">Lèvres Naturelles</option>
                                    <option value="Botox">Botox & Rides</option>
                                    <option value="Skinbooster">Skinbooster</option>
                                </select>
                            </div>
                            <div class="col-md-3 mb-2 mb-md-0">
                                <select id="filterDateRange" onchange="renderPatients()" class="form-control form-control-sm" style="background: #091310; color: #fff; border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; font-size: 12px;">
                                    <option value="all">📅 Toutes dates</option>
                                    <option value="today">Aujourd'hui</option>
                                    <option value="week">7 prochains jours</option>
                                    <option value="month">Ce mois</option>
                                </select>
                            </div>
                            <div class="col-md-5">
                                <div class="input-group input-group-sm">
                                    <input type="text" id="searchInput" oninput="renderPatients()" placeholder="Rechercher nom, tél, note..." class="form-control" style="background: #091310; border: 1px solid rgba(255,255,255,0.15); color: #fff; border-radius: 8px 0 0 8px; font-size: 12px;">
                                    <div class="input-group-append">
                                        <button class="btn btn-outline-secondary" onclick="resetFilters()" title="Réinitialiser" style="border-radius: 0 8px 8px 0; border-color: rgba(255,255,255,0.15); color: var(--gold); font-size: 11px;">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Scrollable Patient Rows -->
                    <div class="patient-table-wrap" id="patientListContainer">
                        <!-- Rendered by JS -->
                    </div>
                </div>
            </div>

            <!-- Right Column: Patient Detail & 1-Click WhatsApp Studio -->
            <div class="col-lg-5">
                <div class="panel-box" id="detailPanel">
                    <div class="panel-header">
                        <div>
                            <h5 class="font-serif font-weight-bold mb-1" style="color: var(--gold-light);">Dossier & Studio WhatsApp</h5>
                            <small class="text-muted">Génération instantanée de message de confirmation</small>
                        </div>
                        <span id="detailStatusBadge" class="patient-badge badge-new">Nouveau</span>
                    </div>

                    <div class="patient-detail-box" id="patientDetailContent">
                        <!-- Patient Info Header -->
                        <div class="p-3 mb-3 rounded-lg" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);">
                            <div class="d-flex justify-content-between align-items-start">
                                <div>
                                    <h5 class="font-weight-bold mb-1 text-white" id="detailName">Sélectionnez une patiente</h5>
                                    <p class="mb-1 text-muted small" id="detailPhone"><i class="fa fa-phone mr-1"></i> --</p>
                                    <span class="badge px-2 py-1 font-weight-bold" style="background: rgba(197, 160, 89, 0.2); color: var(--gold);" id="detailTreatment">--</span>
                                </div>
                                <div class="text-right">
                                    <label class="small text-muted d-block mb-1">Changer Statut :</label>
                                    <select id="detailStatusSelect" onchange="updatePatientStatus(this.value)" class="form-control form-control-sm" style="background: #0f231d; color: var(--gold); border: 1px solid var(--gold); border-radius: 8px;">
                                        <option value="Nouveau">Nouveau</option>
                                        <option value="Contacté">Contacté WhatsApp</option>
                                        <option value="Confirmé">Confirmé</option>
                                        <option value="Réalisé">Séance Réalisée</option>
                                        <option value="Annulé">Annulé</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <!-- 1-Click Message Templates -->
                        <h6 class="small font-weight-bold text-uppercase text-muted mb-2" style="letter-spacing: 1px;">
                            <i class="fa fa-bolt text-gold mr-1"></i> Modèles WhatsApp Prêts à l'Envoi
                        </h6>

                        <!-- Template 1: Confirmation RDV -->
                        <button class="template-btn" onclick="applyTemplate('confirm')">
                            <span>📅 Confirmation de Consultation avec le Dr. Kashi</span>
                            <i class="fa fa-chevron-right text-muted"></i>
                        </button>

                        <!-- Template 2: Rappel Veille -->
                        <button class="template-btn" onclick="applyTemplate('reminder')">
                            <span>🔔 Rappel de RDV (La veille de la séance)</span>
                            <i class="fa fa-chevron-right text-muted"></i>
                        </button>

                        <!-- Template 3: Suivi Post-Traitement J+7 -->
                        <button class="template-btn" onclick="applyTemplate('followup')">
                            <span>✨ Suivi Post-Injection (J+7 Bienveillance)</span>
                            <i class="fa fa-chevron-right text-muted"></i>
                        </button>

                        <!-- Template 4: Darija Pro -->
                        <button class="template-btn" onclick="applyTemplate('darija')">
                            <span>🇲🇦 Message en Darija (Confirmation rapide)</span>
                            <i class="fa fa-chevron-right text-muted"></i>
                        </button>

                        <!-- Live Message Preview Box -->
                        <div class="mt-3">
                            <label class="small text-muted font-weight-bold d-block mb-1">Aperçu du Message à Envoyer :</label>
                            <textarea id="messagePreview" rows="4" class="form-control" style="background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.12); color: #fff; font-size: 13px; border-radius: 12px;"></textarea>
                        </div>

                        <!-- Direct WhatsApp Launch Button -->
                        <div class="mt-3">
                            <button id="sendWaBtn" onclick="launchWhatsApp()" class="btn-wa-direct">
                                <i class="fa fa-whatsapp fa-lg"></i> Ouvrir WhatsApp & Envoyer le Message
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal: Nouveau Patient Manuel -->
    <div class="modal fade" id="newPatientModal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content" style="background: var(--card-dark); border: 1px solid var(--gold); border-radius: 16px; color: #fff;">
                <div class="modal-header border-bottom-0">
                    <h5 class="modal-title font-serif text-gold">Ajouter une Consultation Manuelle</h5>
                    <button type="button" class="close text-white" data-dismiss="modal">&times;</button>
                </div>
                <div class="modal-body">
                    <form id="newPatientForm" onsubmit="saveNewPatient(event)">
                        <div class="form-group">
                            <label class="small text-muted">Nom & Prénom de la Patiente</label>
                            <input type="text" id="m_name" class="form-control" required style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); color: #fff;">
                        </div>
                        <div class="form-group">
                            <label class="small text-muted">Téléphone WhatsApp</label>
                            <input type="tel" id="m_phone" class="form-control" placeholder="06XXXXXXXX" required style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); color: #fff;">
                        </div>
                        <div class="form-group">
                            <label class="small text-muted">Traitement Ciblé</label>
                            <select id="m_treatment" class="form-control" style="background: #091310; border: 1px solid rgba(255,255,255,0.1); color: #fff;">
                                <option value="Vallée des Larmes & Cernes">Vallée des Larmes & Cernes</option>
                                <option value="Pommettes & Restauration Volume">Pommettes & Restauration Volume</option>
                                <option value="Jawline & Profil Texas">Jawline & Profil Texas</option>
                                <option value="Lèvres Naturelles">Lèvres Naturelles</option>
                                <option value="Botox & Rides d'Expression">Botox & Rides d'Expression</option>
                                <option value="Skinbooster & Éclat">Skinbooster & Éclat</option>
                                <option value="Consultation Globale">Consultation Globale</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label class="small text-muted">Date Préférée</label>
                            <input type="date" id="m_date" class="form-control" style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); color: #fff;">
                        </div>
                        <button type="submit" class="btn btn-gold btn-block font-weight-bold mt-4" style="border-radius: 10px;">
                            Enregistrer dans le CRM
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="assets/js/jquery-1.12.4.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>

    <script>
        // Sample Initial Data if empty
        const INITIAL_PATIENTS = [
            {
                id: '1',
                name: 'Zineb B.',
                phone: '0600980685',
                treatment: 'Vallée des Larmes & Pommettes',
                date: '2026-10-12',
                status: 'Confirmé',
                note: 'Patiente du cas vidéo. Perte de volume post-sport. Résultat 100% naturel.'
            },
            {
                id: '2',
                name: 'Sara Benjelloun',
                phone: '0661245890',
                treatment: 'Jawline & Profil Texas',
                date: '2026-10-13',
                status: 'Nouveau',
                note: 'Demande reçue via le diagnostic 1 minute.'
            },
            {
                id: '3',
                name: 'Meryem K.',
                phone: '0663456789',
                treatment: 'Vallée des Larmes & Cernes',
                date: '2026-10-14',
                status: 'Nouveau',
                note: 'Souhaite un regard défatigué avant un événement.'
            },
            {
                id: '4',
                name: 'Leila El Amrani',
                phone: '0672112233',
                treatment: 'Lèvres Naturelles & Hydratation',
                date: '2026-10-15',
                status: 'Contacté',
                note: 'Message de rappel envoyé ce matin.'
            },
            {
                id: '5',
                name: 'Fatima Zahra M.',
                phone: '0660445566',
                treatment: 'Botox & Rides Front',
                date: '2026-10-11',
                status: 'Réalisé',
                note: 'Séance réalisée avec succès sans aucun bleu.'
            }
        ];

        let patients = [];
        let selectedPatientId = null;
        let currentFilter = 'all';

        function loadPatients() {
            const stored = localStorage.getItem('dr_kashi_patients');
            if (stored) {
                try {
                    patients = JSON.parse(stored);
                } catch(e) {
                    patients = INITIAL_PATIENTS;
                }
            } else {
                patients = INITIAL_PATIENTS;
                savePatients();
            }
            if (patients.length > 0 && !selectedPatientId) {
                selectedPatientId = patients[0].id;
            }
            updateKPIs();
            renderPatients();
            renderDetail();
        }

        function savePatients() {
            localStorage.setItem('dr_kashi_patients', JSON.stringify(patients));
            updateKPIs();
        }

        function updateKPIs() {
            const total = patients.length;
            const pending = patients.filter(p => p.status === 'Nouveau' || p.status === 'Contacté').length;
            const contacted = patients.filter(p => p.status === 'Contacté').length;
            const confirmed = patients.filter(p => p.status === 'Confirmé').length;
            const done = patients.filter(p => p.status === 'Réalisé').length;

            document.getElementById('kpi-total').innerText = total + 45; // factoring in past month
            document.getElementById('kpi-pending').innerText = pending;
            document.getElementById('kpi-confirmed').innerText = confirmed + 35;
            
            // Estimated Revenue calculation
            const rev = (confirmed + done + 35) * 2500;
            document.getElementById('kpi-revenue').innerText = rev.toLocaleString() + ' DH';

            document.getElementById('count-all').innerText = total;
            document.getElementById('count-new').innerText = patients.filter(p => p.status === 'Nouveau').length;
            if (document.getElementById('count-contacted')) {
                document.getElementById('count-contacted').innerText = contacted;
            }
            document.getElementById('count-confirmed').innerText = confirmed;
            document.getElementById('count-done').innerText = done;
        }

        function setFilter(f) {
            currentFilter = f;
            document.querySelectorAll('.filter-tab').forEach(b => b.classList.remove('active'));
            if (event && event.target) {
                event.target.classList.add('active');
            }
            renderPatients();
        }

        function resetFilters() {
            currentFilter = 'all';
            document.querySelectorAll('.filter-tab').forEach(b => b.classList.remove('active'));
            const firstTab = document.querySelector('.filter-tab');
            if (firstTab) firstTab.classList.add('active');

            const treatEl = document.getElementById('filterTreatment');
            if (treatEl) treatEl.value = 'all';

            const dateEl = document.getElementById('filterDateRange');
            if (dateEl) dateEl.value = 'all';

            const searchEl = document.getElementById('searchInput');
            if (searchEl) searchEl.value = '';

            renderPatients();
        }

        function renderPatients() {
            const container = document.getElementById('patientListContainer');
            const query = (document.getElementById('searchInput').value || '').toLowerCase();
            const treatmentFilter = document.getElementById('filterTreatment') ? document.getElementById('filterTreatment').value : 'all';
            const dateFilter = document.getElementById('filterDateRange') ? document.getElementById('filterDateRange').value : 'all';

            let filtered = patients;

            // 1. Status Filter
            if (currentFilter !== 'all') {
                filtered = filtered.filter(p => p.status === currentFilter);
            }

            // 2. Treatment Type Filter
            if (treatmentFilter !== 'all') {
                filtered = filtered.filter(p => (p.treatment || '').toLowerCase().includes(treatmentFilter.toLowerCase()));
            }

            // 3. Date Range Filter
            if (dateFilter !== 'all') {
                const now = new Date();
                const todayStr = now.toISOString().slice(0, 10);
                if (dateFilter === 'today') {
                    filtered = filtered.filter(p => p.date === todayStr);
                } else if (dateFilter === 'week') {
                    const nextWeek = new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000).toISOString().slice(0, 10);
                    filtered = filtered.filter(p => p.date >= todayStr && p.date <= nextWeek);
                } else if (dateFilter === 'month') {
                    const currentMonth = todayStr.slice(0, 7);
                    filtered = filtered.filter(p => (p.date || '').startsWith(currentMonth));
                }
            }

            // 4. Free text Search
            if (query) {
                filtered = filtered.filter(p => 
                    (p.name || '').toLowerCase().includes(query) || 
                    (p.phone || '').includes(query) || 
                    (p.treatment || '').toLowerCase().includes(query) ||
                    (p.note || '').toLowerCase().includes(query) ||
                    (p.source || '').toLowerCase().includes(query)
                );
            }

            // Update Counter
            const countBadge = document.getElementById('filterResultsCount');
            if (countBadge) {
                countBadge.innerText = filtered.length + ' résultat(s)';
            }

            if (filtered.length === 0) {
                container.innerHTML = '<div class="text-center py-5 text-muted"><i class="fa fa-user-times fa-2x mb-2"></i><p>Aucune patiente ne correspond aux critères de filtre.</p><button onclick="resetFilters()" class="btn btn-sm btn-outline-warning mt-2">Réinitialiser les filtres</button></div>';
                return;
            }

            let html = '';
            filtered.forEach(p => {
                const isSel = p.id === selectedPatientId ? 'selected' : '';
                let badgeClass = 'badge-new';
                if (p.status === 'Contacté') badgeClass = 'badge-contacted';
                if (p.status === 'Confirmé') badgeClass = 'badge-confirmed';
                if (p.status === 'Réalisé') badgeClass = 'badge-done';
                if (p.status === 'Annulé') badgeClass = 'badge-cancelled';

                html += `
                    <div class="patient-row ${isSel}" onclick="selectPatient('${p.id}')">
                        <div>
                            <strong class="d-block text-white" style="font-size: 15px;">${p.name}</strong>
                            <small class="text-muted"><i class="fa fa-phone mr-1"></i> ${p.phone} • <span style="color: var(--gold);">${p.treatment}</span></small>
                        </div>
                        <div class="text-right">
                            <span class="patient-badge ${badgeClass}">${p.status}</span>
                            <small class="d-block text-muted mt-1" style="font-size: 11px;">${p.date || 'À définir'}</small>
                        </div>
                    </div>
                `;
            });
            container.innerHTML = html;
        }

        function selectPatient(id) {
            selectedPatientId = id;
            renderPatients();
            renderDetail();
        }

        function renderDetail() {
            const p = patients.find(item => item.id === selectedPatientId);
            if (!p) return;

            document.getElementById('detailName').innerText = p.name;
            document.getElementById('detailPhone').innerHTML = '<i class="fa fa-phone mr-1"></i> ' + p.phone;
            document.getElementById('detailTreatment').innerText = p.treatment;
            document.getElementById('detailStatusSelect').value = p.status;

            const badgeEl = document.getElementById('detailStatusBadge');
            badgeEl.innerText = p.status;
            badgeEl.className = 'patient-badge ';
            if (p.status === 'Nouveau') badgeEl.classList.add('badge-new');
            else if (p.status === 'Contacté') badgeEl.classList.add('badge-contacted');
            else if (p.status === 'Confirmé') badgeEl.classList.add('badge-confirmed');
            else if (p.status === 'Réalisé') badgeEl.classList.add('badge-done');
            else badgeEl.classList.add('badge-cancelled');

            // Default template
            applyTemplate('confirm');
        }

        function updatePatientStatus(newStatus) {
            const p = patients.find(item => item.id === selectedPatientId);
            if (p) {
                p.status = newStatus;
                savePatients();
                renderPatients();
                renderDetail();
            }
        }

        function applyTemplate(type) {
            const p = patients.find(item => item.id === selectedPatientId);
            if (!p) return;

            let msg = '';
            if (type === 'confirm') {
                msg = `Bonjour ${p.name}, c'est le secrétariat du Dr. Hanane Kashi à Casablanca.\\n\\nNous avons bien reçu votre demande pour le traitement : ${p.treatment}.\\nLe Dr. Kashi a réservé un créneau pour votre consultation personnalisée ce ${p.date || 'très prochainement'}.\\n\\nEst-ce que cette date vous convient pour vous accueillir au cabinet ?`;
            } else if (type === 'reminder') {
                msg = `Bonjour ${p.name}, rappel bienveillant de votre rendez-vous de consultation avec le Dr. Hanane Kashi prévu demain à notre cabinet à Casablanca.\\n\\nAdresse : Casablanca, Maroc.\\nPour toute question avant votre arrivée, nous restons à votre disposition au 05 20 60 44 84. À demain !`;
            } else if (type === 'followup') {
                msg = `Bonjour ${p.name}, le Dr. Hanane Kashi espère que vous vous portez à merveille après votre séance de ${p.treatment} !\\n\\nComment se passe votre récupération ? Avez-vous la moindre question ?\\nN'hésitez pas à nous envoyer une photo ou à nous appeler si nécessaire. Prenez bien soin de vous !`;
            } else if (type === 'darija') {
                msg = `Salam khti ${p.name}, m3ak secrétariat dial Dr. Hanane Kashi f Casablanca.\\n\\nTwaslna b la demande dyalk bkhousous : ${p.treatment}.\\nBghina n-confirmiw m3ak l'rendez-vous nhar ${p.date || '9riban'}. Wach had l'wa9t mnasbek bach n-blokiw lik l'créneau ?`;
            }

            document.getElementById('messagePreview').value = msg;
        }

        function launchWhatsApp() {
            const p = patients.find(item => item.id === selectedPatientId);
            if (!p) return;

            const msg = document.getElementById('messagePreview').value;
            let cleanPhone = p.phone.replace(/\\s+/g, '').replace(/^0/, '212');
            if (!cleanPhone.startsWith('212')) {
                cleanPhone = '212' + cleanPhone;
            }

            // Mark as contacted automatically
            if (p.status === 'Nouveau') {
                p.status = 'Contacté';
                savePatients();
                renderPatients();
                renderDetail();
            }

            const url = `https://wa.me/${cleanPhone}?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank');
        }

        function openNewPatientModal() {
            $('#newPatientModal').modal('show');
        }

        function saveNewPatient(e) {
            e.preventDefault();
            const name = document.getElementById('m_name').value.trim();
            const phone = document.getElementById('m_phone').value.trim();
            const treatment = document.getElementById('m_treatment').value;
            const date = document.getElementById('m_date').value;

            const newP = {
                id: Date.now().toString(),
                name,
                phone,
                treatment,
                date,
                status: 'Nouveau',
                note: 'Ajout manuel depuis le secrétariat.'
            };

            patients.unshift(newP);
            selectedPatientId = newP.id;
            savePatients();
            $('#newPatientModal').modal('hide');
            document.getElementById('newPatientForm').reset();
            renderPatients();
            renderDetail();
        }

        function exportToCsv() {
            let csv = 'ID,Nom,Telephone,Traitement,Date,Statut,Notes\\n';
            patients.forEach(p => {
                csv += `"${p.id}","${p.name}","${p.phone}","${p.treatment}","${p.date}","${p.status}","${p.note || ''}"\\n`;
            });
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.setAttribute('download', 'patientes_dr_kashi_' + new Date().toISOString().slice(0,10) + '.csv');
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }

        // Init
        document.addEventListener('DOMContentLoaded', loadPatients);
    </script>
</body>
</html>
"""

def main():
    target = CLINIC_DIR / "admin.html"
    target.write_text(ADMIN_HTML, encoding="utf-8")
    print(f"✅ Created Aesthetic Clinic CRM & Admin Dashboard at: {target}")

if __name__ == "__main__":
    main()
