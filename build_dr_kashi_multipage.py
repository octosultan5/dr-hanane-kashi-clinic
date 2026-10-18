# -*- coding: utf-8 -*-
"""
Builds a complete, prestigious multi-page clinic ecosystem for Dr. Hanane Kashi:
- Updates index.html with multi-page navigation + "Pages" dropdown
- Generates 7 dedicated pages:
  1. a-propos.html (Cabinet, Bio, Medical Ethics, Safety)
  2. traitements.html (Catalog of Injectables, Botox, Skinbooster, Peeling)
  3. avant-apres.html (Interactive Before/After Sliders & Case Studies)
  4. tarifs.html (Transparent Medical Fees in MAD & Inclusions)
  5. temoignages.html (Real Patient Reviews & Verified Ratings)
  6. faq.html (In-depth Medical FAQ Accordion)
  7. contact.html (Interactive Booking Form, Clinic Map, Opening Hours)
"""

import sys
from pathlib import Path
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CLINIC_DIR = Path(r"C:\Users\USER\.gemini\antigravity\scratch\dr-hanane-kashi-clinic")

# Common Header & Nav Generator
def get_header(active_page="index"):
    nav_links = [
        ("Accueil", "index.html", "index"),
        ("Le Cabinet", "a-propos.html", "a-propos"),
        ("Traitements", "traitements.html", "traitements"),
        ("Avant / Après", "avant-apres.html", "avant-apres"),
        ("Tarifs", "tarifs.html", "tarifs"),
        ("Témoignages", "temoignages.html", "temoignages"),
        ("FAQ", "faq.html", "faq"),
        ("Contact", "contact.html", "contact"),
    ]
    
    links_html = ""
    for label, url, key in nav_links:
        cls = ' class="active"' if active_page == key else ""
        links_html += f'<li{cls}><a href="{url}">{label}</a></li>\n'
        
    dropdown_html = f'''
        <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span style="color: #c5a059; font-weight: 700;">Pages</span> <i class="fa fa-angle-down"></i></a>
            <ul class="dropdown-menu">
                <li><a href="a-propos.html"><i class="fa fa-user-md mr-2" style="color: #c5a059;"></i> Le Cabinet & Dr. Kashi</a></li>
                <li><a href="traitements.html"><i class="fa fa-magic mr-2" style="color: #c5a059;"></i> Catalogue des Soins</a></li>
                <li><a href="avant-apres.html"><i class="fa fa-sliders mr-2" style="color: #c5a059;"></i> Galerie Avant / Après</a></li>
                <li><a href="tarifs.html"><i class="fa fa-tag mr-2" style="color: #c5a059;"></i> Honoraires & Forfaits</a></li>
                <li><a href="temoignages.html"><i class="fa fa-star mr-2" style="color: #c5a059;"></i> Avis Patientes</a></li>
                <li><a href="faq.html"><i class="fa fa-question-circle mr-2" style="color: #c5a059;"></i> Questions Fréquentes</a></li>
                <li><a href="contact.html"><i class="fa fa-map-marker mr-2" style="color: #c5a059;"></i> Accès & Contact</a></li>
                <li class="divider"></li>
                <li><a href="admin.html"><i class="fa fa-lock mr-2" style="color: #0f4c3a;"></i> Espace Secrétariat (CRM)</a></li>
            </ul>
        </li>
    '''
    
    return f'''
    <!-- Topbar Info -->
    <div class="top-bar-area bg-emerald text-light py-2" style="font-size: 13px; border-bottom: 1px solid rgba(197, 160, 89, 0.3);">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-7 col-12 text-center text-md-left">
                    <span class="mr-3"><i class="fas fa-map-marker-alt text-gold mr-1"></i> Casablanca, Quartier Gauthier</span>
                    <span><i class="fas fa-clock text-gold mr-1"></i> Lun - Sam : 09h00 - 19h00</span>
                </div>
                <div class="col-md-5 col-12 text-center text-md-right mt-1 mt-md-0 d-flex justify-content-center justify-content-md-end align-items-center">
                    <a href="tel:+212600980685" class="text-light mr-3 font-weight-bold"><i class="fas fa-phone-alt text-gold mr-1"></i> +212 600 980 685</a>
                    <div class="lang-switch d-inline-flex align-items-center" style="background: rgba(255,255,255,0.1); padding: 2px 10px; border-radius: 20px;">
                        <a href="index.html" style="color: #c5a059; font-weight: bold; font-size: 11px;">FR</a>
                        <span class="text-muted mx-1" style="font-size: 10px;">|</span>
                        <a href="ar.html" style="color: #fff; font-size: 11px;">عربي</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Navigation -->
    <header id="home">
        <nav class="navbar navbar-default navbar-sticky bootsnav">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-menu">
                        <i class="fa fa-bars"></i>
                    </button>
                    <a class="navbar-brand d-flex align-items-center" href="index.html" style="padding: 6px 0;">
                        <img src="assets/img/dr-kashi-logo.jpg" alt="Logo Dr Hanane Kashi" style="height: 50px; width: 50px; border-radius: 50%; object-fit: cover; border: 2px solid #c5a059;" class="mr-2">
                        <div style="line-height: 1.2;">
                            <span class="font-serif font-weight-bold" style="font-size: 21px; color: var(--primary-emerald); letter-spacing: -0.5px;">Dr. Hanane Kashi</span>
                            <span class="d-block text-muted" style="font-size: 10px; text-transform: uppercase; letter-spacing: 2px;">Médecine Esthétique & Laser</span>
                        </div>
                    </a>
                </div>

                <div class="collapse navbar-collapse" id="navbar-menu">
                    <ul class="nav navbar-nav navbar-right" data-in="fadeInDown" data-out="fadeOutUp">
                        {links_html}
                        {dropdown_html}
                        <li class="d-none d-lg-block ml-2">
                            <a href="contact.html" class="btn-gold" style="padding: 8px 20px !important; margin-top: 18px; color: #fff !important; font-size: 12px;">Prendre RDV</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
    '''

# Common Footer Generator
def get_footer():
    return '''
    <!-- Footer -->
    <footer class="bg-dark text-light pt-5 pb-3" style="background: #09261d !important; border-top: 3px solid #c5a059;">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="d-flex align-items-center mb-3">
                        <img src="assets/img/dr-kashi-logo.jpg" alt="Dr Kashi" style="height: 50px; width: 50px; border-radius: 50%; border: 2px solid #c5a059;" class="mr-3">
                        <div>
                            <h4 class="font-serif text-white mb-0" style="font-size: 20px;">Docteur Hanane Kashi</h4>
                            <small class="text-gold text-uppercase" style="letter-spacing: 1px;">Médecine Esthétique & Anti-Âge</small>
                        </div>
                    </div>
                    <p class="text-muted small" style="line-height: 1.6;">
                        Cabinet d'excellence dédié à l'harmonie et à la mise en valeur naturelle de votre visage. Des protocoles médicaux stricts, des produits certifiés CE & FDA et un suivi rigoureux.
                    </p>
                    <div class="d-flex gap-2">
                        <a href="https://wa.me/212600980685" target="_blank" class="btn btn-sm btn-outline-light" style="border-radius: 20px;"><i class="fab fa-whatsapp text-gold"></i> WhatsApp</a>
                        <a href="tel:+212600980685" class="btn btn-sm btn-outline-light" style="border-radius: 20px;"><i class="fas fa-phone-alt text-gold"></i> Appel Direct</a>
                    </div>
                </div>

                <div class="col-lg-2 col-md-6 mb-4">
                    <h5 class="text-gold font-serif mb-3">Navigation</h5>
                    <ul class="list-unstyled small text-muted">
                        <li class="mb-2"><a href="index.html" class="text-light text-decoration-none">Accueil</a></li>
                        <li class="mb-2"><a href="a-propos.html" class="text-light text-decoration-none">Le Cabinet</a></li>
                        <li class="mb-2"><a href="traitements.html" class="text-light text-decoration-none">Traitements</a></li>
                        <li class="mb-2"><a href="avant-apres.html" class="text-light text-decoration-none">Avant / Après</a></li>
                        <li class="mb-2"><a href="tarifs.html" class="text-light text-decoration-none">Honoraires</a></li>
                        <li class="mb-2"><a href="temoignages.html" class="text-light text-decoration-none">Avis Patientes</a></li>
                        <li class="mb-2"><a href="faq.html" class="text-light text-decoration-none">FAQ Médicale</a></li>
                        <li class="mb-2"><a href="contact.html" class="text-light text-decoration-none">Accès & Contact</a></li>
                    </ul>
                </div>

                <div class="col-lg-3 col-md-6 mb-4">
                    <h5 class="text-gold font-serif mb-3">Soins Phares</h5>
                    <ul class="list-unstyled small text-muted">
                        <li class="mb-2"><a href="traitements.html#levres" class="text-light text-decoration-none">• Injections Lèvres & Russian Lips</a></li>
                        <li class="mb-2"><a href="traitements.html#cernes" class="text-light text-decoration-none">• Comblement Cernes Creux</a></li>
                        <li class="mb-2"><a href="traitements.html#botox" class="text-light text-decoration-none">• Toxine Botulique (Front & Lion)</a></li>
                        <li class="mb-2"><a href="traitements.html#jawline" class="text-light text-decoration-none">• Jawline Contouring & Menton</a></li>
                        <li class="mb-2"><a href="traitements.html#profhilo" class="text-light text-decoration-none">• Skinbooster & Profhilo Glow</a></li>
                    </ul>
                </div>

                <div class="col-lg-3 col-md-6 mb-4">
                    <h5 class="text-gold font-serif mb-3">Coordonnées</h5>
                    <ul class="list-unstyled small text-muted">
                        <li class="mb-2"><i class="fas fa-map-marker-alt text-gold mr-2"></i> Boulevard d'Anfa / Gauthier, Casablanca</li>
                        <li class="mb-2"><i class="fas fa-phone-alt text-gold mr-2"></i> +212 600 980 685</li>
                        <li class="mb-2"><i class="fas fa-envelope text-gold mr-2"></i> contact@drhananekashi.ma</li>
                        <li class="mb-2"><i class="fas fa-clock text-gold mr-2"></i> Lun - Ven : 09h00 - 19h00<br><span class="ml-4">Samedi : 09h00 - 14h00</span></li>
                    </ul>
                </div>
            </div>

            <hr style="border-color: rgba(255,255,255,0.1);">
            <div class="row align-items-center small text-muted">
                <div class="col-md-6 text-center text-md-left">
                    &copy; 2026 Cabinet Dr. Hanane Kashi. Tous droits réservés. Réalisation d'élite par <strong class="text-gold">Ghaya Prod</strong>.
                </div>
                <div class="col-md-6 text-center text-md-right mt-2 mt-md-0">
                    <a href="admin.html" class="text-muted mr-3"><i class="fas fa-lock text-gold"></i> Secrétariat CRM</a>
                    <a href="contact.html" class="text-muted">Mentions Légales & Confidentialité</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp -->
    <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20une%20consultation." target="_blank" class="floating-whatsapp" title="Contacter sur WhatsApp">
        <i class="fab fa-whatsapp"></i>
    </a>

    <!-- Sticky Mobile Bar -->
    <div class="sticky-mobile-bar">
        <a href="tel:+212600980685" class="sticky-call">
            <i class="fas fa-phone-alt"></i> Appeler le Cabinet
        </a>
        <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20une%20consultation." target="_blank" class="sticky-wa">
            <i class="fab fa-whatsapp"></i> WhatsApp Direct
        </a>
    </div>

    <!-- Scripts -->
    <script src="assets/js/jquery-1.12.4.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/equal-height.min.js"></script>
    <script src="assets/js/jquery.appear.js"></script>
    <script src="assets/js/jquery.easing.min.js"></script>
    <script src="assets/js/jquery.magnific-popup.min.js"></script>
    <script src="assets/js/modernizr.custom.13711.js"></script>
    <script src="assets/js/owl.carousel.min.js"></script>
    <script src="assets/js/wow.min.js"></script>
    <script src="assets/js/progress-bar.min.js"></script>
    <script src="assets/js/isotope.pkgd.min.js"></script>
    <script src="assets/js/imagesloaded.pkgd.min.js"></script>
    <script src="assets/js/count-to.js"></script>
    <script src="assets/js/YTPlayer.min.js"></script>
    <script src="assets/js/bootsnav.js"></script>
    <script src="assets/js/main.js"></script>

    <script>
    // Lead Storage Helper
    function recordPatientInCRM(name, phone, treatment, date, source, note) {
        try {
            var list = [];
            var stored = localStorage.getItem('dr_kashi_patients');
            if (stored) {
                list = JSON.parse(stored);
            }
            var newLead = {
                id: Date.now().toString(),
                name: name || 'Patiente Web',
                phone: phone || '',
                treatment: treatment || 'Consultation Globale',
                date: date || new Date().toISOString().slice(0, 10),
                status: 'Nouveau',
                source: source || 'Site Web',
                note: note || ('Demande reçue via ' + (source || 'Site Web'))
            };
            list.unshift(newLead);
            localStorage.setItem('dr_kashi_patients', JSON.stringify(list));
        } catch(e) {
            console.error("Erreur enregistrement CRM :", e);
        }
    }
    </script>
    '''

# Common HTML Shell Wrapper
def wrap_page(title, active_page, body_content, extra_head=""):
    return f'''<!DOCTYPE html>
<html lang="fr" dir="ltr">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Docteur Hanane Kashi - Médecine Esthétique & Anti-Âge à Casablanca. Injections d'acide hyaluronique, botox, comblement des cernes, harmonisation faciale naturelle.">
    <title>{title} | Dr. Hanane Kashi Casablanca</title>
    <link rel="shortcut icon" href="assets/img/dr-kashi-logo.jpg" type="image/x-icon">

    <!-- CSS Assets -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />
    <link href="assets/css/font-awesome.min.css" rel="stylesheet" />
    <link href="assets/css/themify-icons.css" rel="stylesheet" />
    <link href="assets/css/flaticon-set.css" rel="stylesheet" />
    <link href="assets/css/magnific-popup.css" rel="stylesheet" />
    <link href="assets/css/owl.carousel.min.css" rel="stylesheet" />
    <link href="assets/css/owl.theme.default.min.css" rel="stylesheet" />
    <link href="assets/css/animate.css" rel="stylesheet" />
    <link href="assets/css/bootsnav.css" rel="stylesheet" />
    <link href="style.css" rel="stylesheet">
    <link href="assets/css/responsive.css" rel="stylesheet" />

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --primary-emerald: #0f4c3a;
            --primary-gold: #c5a059;
            --primary-accent: #1ebeb6;
            --text-dark: #1e293b;
        }}
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #334155;
            background-color: #ffffff;
            overflow-x: hidden;
        }}
        h1, h2, h3, h4, .font-serif {{
            font-family: 'Playfair Display', serif;
        }}
        .bg-emerald {{ background-color: var(--primary-emerald) !important; }}
        .text-emerald {{ color: var(--primary-emerald) !important; }}
        .text-gold {{ color: var(--primary-gold) !important; }}
        
        .btn-gold {{
            background: linear-gradient(135deg, #d4af37, #c5a059);
            color: #fff !important;
            border: none;
            padding: 13px 26px;
            font-weight: 700;
            border-radius: 50px;
            box-shadow: 0 10px 25px rgba(197, 160, 89, 0.4);
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
        }}
        .btn-gold:hover {{
            background: linear-gradient(135deg, #c5a059, #b08d46);
            transform: translateY(-2px);
            color: #fff !important;
        }}
        .btn-whatsapp {{
            background: #25D366;
            color: #fff !important;
            padding: 13px 26px;
            font-weight: 700;
            border-radius: 50px;
            border: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 8px 20px rgba(37, 211, 102, 0.35);
            transition: all 0.3s ease;
            text-decoration: none;
        }}
        .btn-whatsapp:hover {{
            background: #1eb956;
            transform: translateY(-2px);
            color: #fff;
        }}
        .floating-whatsapp {{
            position: fixed;
            bottom: 85px;
            right: 25px;
            background: #25D366;
            color: #fff !important;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 8px 30px rgba(37, 211, 102, 0.6);
            z-index: 9999;
            transition: transform 0.3s ease;
            animation: pulse-green 2s infinite;
            text-decoration: none;
        }}
        .floating-whatsapp:hover {{ transform: scale(1.1); }}
        @keyframes pulse-green {{
            0% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }}
            70% {{ box-shadow: 0 0 0 16px rgba(37, 211, 102, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }}
        }}
        .sticky-mobile-bar {{
            position: fixed;
            bottom: 0; left: 0;
            width: 100%;
            background: rgba(15, 76, 58, 0.98);
            backdrop-filter: blur(10px);
            padding: 10px 15px;
            display: flex;
            gap: 10px;
            z-index: 9998;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
        }}
        .sticky-mobile-bar a {{
            flex: 1;
            text-align: center;
            padding: 12px 10px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 13px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            text-decoration: none;
        }}
        .sticky-call {{ background: #ffffff; color: #0f4c3a !important; }}
        .sticky-wa {{ background: #25D366; color: #ffffff !important; }}
        @media (min-width: 992px) {{
            .sticky-mobile-bar {{ display: none; }}
            .floating-whatsapp {{ bottom: 30px; }}
        }}
        .page-banner {{
            background: linear-gradient(135deg, rgba(15, 76, 58, 0.95) 0%, rgba(10, 45, 35, 0.97) 100%), url('assets/img/dr-kashi-hero-banner.jpg') center/cover no-repeat;
            padding: 110px 0 80px;
            color: #fff;
            text-align: center;
        }}
        .badge-gold {{
            background: rgba(197, 160, 89, 0.2);
            color: #fce7b2;
            border: 1px solid #c5a059;
            padding: 6px 16px;
            border-radius: 30px;
            font-size: 12px;
            letter-spacing: 1.5px;
            display: inline-block;
            margin-bottom: 15px;
            text-transform: uppercase;
        }}
        .clinic-card {{
            background: #fff;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            border: 1px solid #f1f5f9;
            transition: all 0.3s ease;
            height: 100%;
        }}
        .clinic-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 18px 40px rgba(15, 76, 58, 0.12);
            border-color: #c5a059;
        }}
        {extra_head}
    </style>
</head>
<body>
    {get_header(active_page)}
    {body_content}
    {get_footer()}
</body>
</html>
'''

print("Starting generation of Dr. Hanane Kashi multi-page website...")

# ==========================================
# 1. Update index.html Header Navigation
# ==========================================
with open(CLINIC_DIR / "index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Replace header in index.html to include multi-page links and dropdown
old_header_pat = r'<div class="top-bar-area[\s\S]*?</header>'
new_header = get_header("index").strip()
if re.search(old_header_pat, idx_content):
    idx_content = re.sub(old_header_pat, new_header, idx_content, count=1)
    (CLINIC_DIR / "index.html").write_text(idx_content, encoding="utf-8")
    print("✅ index.html updated with multi-page navigation & Pages dropdown!")
else:
    print("⚠️ Could not match old header in index.html, check regex.")

# ==========================================
# 2. Page: a-propos.html (Le Cabinet & Dr. Kashi)
# ==========================================
about_body = '''
    <!-- Page Banner -->
    <div class="page-banner">
        <div class="container">
            <span class="badge-gold">Excellence & Éthique Médicale</span>
            <h1 class="display-4 font-weight-bold mb-3 font-serif">Le Cabinet & Le Dr. Hanane Kashi</h1>
            <p class="lead max-w-700 mx-auto" style="color: #cbd5e1; max-width: 700px; margin: 0 auto;">
                Une approche médicale raffinée alliant rigueur anatomique, bienveillance et discrétion absolue au cœur de Casablanca.
            </p>
        </div>
    </div>

    <!-- Doctor Presentation -->
    <div class="py-5" style="background: #fafaf9;">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-5 mb-4 mb-lg-0 text-center">
                    <div style="border-radius: 24px; overflow: hidden; border: 4px solid #c5a059; box-shadow: 0 15px 40px rgba(0,0,0,0.12); max-width: 420px; margin: 0 auto;">
                        <img src="assets/img/dr-kashi-desk.png" alt="Docteur Hanane Kashi" class="img-fluid w-100">
                    </div>
                </div>
                <div class="col-lg-7 pl-lg-5">
                    <span class="badge px-3 py-2 text-uppercase mb-2" style="background: rgba(15,76,58,0.1); color: #0f4c3a; font-weight: 700;">Parcours & Vision</span>
                    <h2 class="font-serif font-weight-bold mb-3" style="color: #0f4c3a; font-size: 34px;">
                        « Sublimer sans figer, harmoniser sans transformer. »
                    </h2>
                    <p class="text-muted" style="line-height: 1.8; font-size: 16px;">
                        Diplômée de la Faculté de Médecine et titulaire de formations internationales approfondies en injectables et médecine morphologique anti-âge (Paris & Casablanca), le <strong>Dr. Hanane Kashi</strong> met son expertise anatomique au service d'une beauté vivante, naturelle et élégante.
                    </p>
                    <p class="text-muted" style="line-height: 1.8; font-size: 16px;">
                        Chaque visage a une histoire, des proportions uniques et une dynamique d'expression qu'il faut savoir respecter. L'objectif n'est jamais de standardiser les traits, mais de défatiguer un regard, de restaurer les volumes délicatement affaissés avec le temps, et de révéler votre propre éclat avec une totale discrétion.
                    </p>
                    <div class="row mt-4">
                        <div class="col-sm-4 text-center mb-3">
                            <div class="p-3 bg-white rounded shadow-sm border">
                                <h3 class="font-serif text-emerald font-weight-bold mb-1">10+</h3>
                                <small class="text-muted font-weight-bold">Années d'Excellence</small>
                            </div>
                        </div>
                        <div class="col-sm-4 text-center mb-3">
                            <div class="p-3 bg-white rounded shadow-sm border">
                                <h3 class="font-serif text-emerald font-weight-bold mb-1">100%</h3>
                                <small class="text-muted font-weight-bold">Traçabilité CE & FDA</small>
                            </div>
                        </div>
                        <div class="col-sm-4 text-center mb-3">
                            <div class="p-3 bg-white rounded shadow-sm border">
                                <h3 class="font-serif text-emerald font-weight-bold mb-1">4.9/5</h3>
                                <small class="text-muted font-weight-bold">Satisfaction Patientes</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 4 Pillars of Medical Excellence -->
    <div class="py-5 bg-white">
        <div class="container py-4">
            <div class="text-center mb-5">
                <span class="badge-gold">Nos Engagements</span>
                <h2 class="font-serif font-weight-bold" style="color: #0f4c3a;">Les 4 Piliers du Cabinet Dr. Kashi</h2>
            </div>
            <div class="row">
                <div class="col-md-6 col-lg-3 mb-4">
                    <div class="clinic-card text-center">
                        <div class="mb-3" style="width: 65px; height: 65px; background: rgba(197,160,89,0.15); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">
                            <i class="fas fa-stethoscope text-gold" style="font-size: 26px;"></i>
                        </div>
                        <h4 class="font-serif font-weight-bold mb-2">Diagnostic 360°</h4>
                        <p class="text-muted small">Analyse minutieuse de la morphologie faciale, de l'élasticité cutanée et de vos attentes avant tout geste médical.</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3 mb-4">
                    <div class="clinic-card text-center">
                        <div class="mb-3" style="width: 65px; height: 65px; background: rgba(15,76,58,0.15); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">
                            <i class="fas fa-shield-alt text-emerald" style="font-size: 26px;"></i>
                        </div>
                        <h4 class="font-serif font-weight-bold mb-2">Sécurité & Pureté</h4>
                        <p class="text-muted small">Utilisation exclusive d'acides hyaluroniques et toxines de classe mondiale (Juvéderm, Teoxane, Restylane) scellés et étiquetés.</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3 mb-4">
                    <div class="clinic-card text-center">
                        <div class="mb-3" style="width: 65px; height: 65px; background: rgba(197,160,89,0.15); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">
                            <i class="fas fa-feather-alt text-gold" style="font-size: 26px;"></i>
                        </div>
                        <h4 class="font-serif font-weight-bold mb-2">Geste Doux Atrauma</h4>
                        <p class="text-muted small">Injection à la micro-canule à bout mousse pour prévenir les hématomes, limiter la douleur et garantir une reprise immédiate.</p>
                    </div>
                </div>
                <div class="col-md-6 col-lg-3 mb-4">
                    <div class="clinic-card text-center">
                        <div class="mb-3" style="width: 65px; height: 65px; background: rgba(15,76,58,0.15); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">
                            <i class="fas fa-user-check text-emerald" style="font-size: 26px;"></i>
                        </div>
                        <h4 class="font-serif font-weight-bold mb-2">Suivi Post-Acte</h4>
                        <p class="text-muted small">Consultation de contrôle systématique à 15 jours offerte avec retouche millimétrique incluse si nécessaire.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- CTA Box -->
    <div class="py-5 bg-emerald text-white text-center">
        <div class="container py-3">
            <h2 class="font-serif font-weight-bold mb-3">Envie d'un avis d'expert sur votre visage ?</h2>
            <p class="lead mb-4 text-light max-w-600 mx-auto" style="max-width: 600px; margin: 0 auto;">
                Prenez rendez-vous directement pour une consultation d'évaluation privée avec le Dr. Hanane Kashi.
            </p>
            <a href="contact.html" class="btn-gold mr-3 mb-2"><i class="fas fa-calendar-alt"></i> Prendre Rendez-vous</a>
            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20des%20renseignements%20sur%20le%20cabinet." target="_blank" class="btn-whatsapp mb-2"><i class="fab fa-whatsapp"></i> Écrire sur WhatsApp</a>
        </div>
    </div>
'''
(CLINIC_DIR / "a-propos.html").write_text(wrap_page("Le Cabinet & Dr. Hanane Kashi", "a-propos", about_body), encoding="utf-8")
print("✅ a-propos.html created!")

# ==========================================
# 3. Page: traitements.html (Catalogue Soins)
# ==========================================
treatments_body = '''
    <!-- Page Banner -->
    <div class="page-banner">
        <div class="container">
            <span class="badge-gold">Expertise Médicale Avancée</span>
            <h1 class="display-4 font-weight-bold mb-3 font-serif">Catalogue des Traitements & Soins</h1>
            <p class="lead max-w-700 mx-auto" style="color: #cbd5e1; max-width: 700px; margin: 0 auto;">
                Injections d'acide hyaluronique haute précision, toxine botulique lissante et soins de bio-régénération cutanée.
            </p>
        </div>
    </div>

    <!-- Treatments Grid -->
    <div class="py-5" style="background: #f8fafc;">
        <div class="container py-4">

            <!-- Section 1: Injections Acide Hyaluronique -->
            <div class="mb-5" id="acide-hyaluronique">
                <div class="d-flex align-items-center mb-4">
                    <span class="mr-3" style="width: 40px; height: 40px; background: #c5a059; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: bold;">01</span>
                    <div>
                        <h2 class="font-serif font-weight-bold text-emerald mb-0">Injections d'Acide Hyaluronique</h2>
                        <small class="text-muted">Restauration des volumes, comblement des rides et harmonisation des proportions</small>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 mb-4" id="levres">
                        <div class="clinic-card">
                            <span class="badge badge-success mb-2" style="background: #0f4c3a;">Très Demandé</span>
                            <h4 class="font-serif font-weight-bold mb-2">Lèvres & Russian Lips</h4>
                            <p class="text-muted small">Dessin précis de l'arc de cupidon, réhydratation en profondeur et projection élégante sans effet canard.</p>
                            <ul class="list-unstyled small text-muted mb-4">
                                <li><i class="fas fa-check text-gold mr-2"></i> Durée de séance : 30 min</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Tenue : 9 à 12 mois</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Anesthésie locale intégrée</li>
                            </ul>
                            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20pour%20les%20L%C3%A8vres." target="_blank" class="btn btn-sm btn-outline-success btn-block rounded-pill font-weight-bold">
                                <i class="fab fa-whatsapp"></i> Réserver pour les Lèvres
                            </a>
                        </div>
                    </div>

                    <div class="col-lg-4 col-md-6 mb-4" id="cernes">
                        <div class="clinic-card">
                            <span class="badge badge-info mb-2" style="background: #c5a059;">Spécialité</span>
                            <h4 class="font-serif font-weight-bold mb-2">Comblement Cernes Creux</h4>
                            <p class="text-muted small">Micro-canule atraumatique pour effacer l'ombre fatiguée sous l'œil sans risque de poches ou d'œdème.</p>
                            <ul class="list-unstyled small text-muted mb-4">
                                <li><i class="fas fa-check text-gold mr-2"></i> Regard instantanément défatigué</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Tenue : 12 à 18 mois</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Produit spécifique ultra-fluide</li>
                            </ul>
                            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20pour%20les%20Cernes." target="_blank" class="btn btn-sm btn-outline-success btn-block rounded-pill font-weight-bold">
                                <i class="fab fa-whatsapp"></i> Réserver pour les Cernes
                            </a>
                        </div>
                    </div>

                    <div class="col-lg-4 col-md-6 mb-4" id="jawline">
                        <div class="clinic-card">
                            <span class="badge badge-secondary mb-2" style="background: #334155;">Profiloplastie</span>
                            <h4 class="font-serif font-weight-bold mb-2">Jawline & Menton</h4>
                            <p class="text-muted small">Redéfinition nette de l'angle mandibulaire et projection du menton pour affiner l'ovale et gommer le double menton débutant.</p>
                            <ul class="list-unstyled small text-muted mb-4">
                                <li><i class="fas fa-check text-gold mr-2"></i> Ovale du visage sculpté</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Tenue : 12 à 18 mois</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Acide hyaluronique haute densité</li>
                            </ul>
                            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20pour%20la%20Jawline." target="_blank" class="btn btn-sm btn-outline-success btn-block rounded-pill font-weight-bold">
                                <i class="fab fa-whatsapp"></i> Réserver pour la Jawline
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Section 2: Toxine Botulique (Botox) -->
            <div class="mb-5" id="botox">
                <div class="d-flex align-items-center mb-4">
                    <span class="mr-3" style="width: 40px; height: 40px; background: #0f4c3a; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: bold;">02</span>
                    <div>
                        <h2 class="font-serif font-weight-bold text-emerald mb-0">Toxine Botulique (Botox Médical)</h2>
                        <small class="text-muted">Relaxation ciblée des muscles hyperactifs pour effacer les rides d'expression tout en préservant le naturel</small>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 mb-4">
                        <div class="clinic-card">
                            <h4 class="font-serif font-weight-bold mb-2">Front & Ride du Lion</h4>
                            <p class="text-muted small">Lissage délicat des lignes horizontales du front et de la ride de la glabelle pour adoucir le regard sans figer.</p>
                            <ul class="list-unstyled small text-muted mb-4">
                                <li><i class="fas fa-check text-gold mr-2"></i> Effet visible dès le 4e jour</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Repos musculaire complet à 15 jours</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Tenue : 4 à 6 mois</li>
                            </ul>
                            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20un%20RDV%20pour%20le%20Front%20et%20Ride%20du%20Lion." target="_blank" class="btn btn-sm btn-outline-success btn-block rounded-pill font-weight-bold">
                                <i class="fab fa-whatsapp"></i> Réserver Consultation Botox
                            </a>
                        </div>
                    </div>

                    <div class="col-lg-4 col-md-6 mb-4">
                        <div class="clinic-card">
                            <h4 class="font-serif font-weight-bold mb-2">Pattes d'Oie & Bunny Lines</h4>
                            <p class="text-muted small">Estompage des ridules du coin des yeux et de la racine du nez tout en maintenant le sourire éclatant.</p>
                            <ul class="list-unstyled small text-muted mb-4">
                                <li><i class="fas fa-check text-gold mr-2"></i> Évite le plissement marqué</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Traitement rapide en 15 min</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Reprise immédiate des activités</li>
                            </ul>
                            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20un%20RDV%20pour%20les%20Pattes%20d%27Oie." target="_blank" class="btn btn-sm btn-outline-success btn-block rounded-pill font-weight-bold">
                                <i class="fab fa-whatsapp"></i> Réserver Pattes d'Oie
                            </a>
                        </div>
                    </div>

                    <div class="col-lg-4 col-md-6 mb-4">
                        <div class="clinic-card">
                            <h4 class="font-serif font-weight-bold mb-2">Masséters & Bruxisme</h4>
                            <p class="text-muted small">Affinement du bas du visage trop carré et soulagement immédiat des tensions de la mâchoire et du grincement nocturne.</p>
                            <ul class="list-unstyled small text-muted mb-4">
                                <li><i class="fas fa-check text-gold mr-2"></i> Effet affinant en V-Shape</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Confort articulaire restauré</li>
                                <li><i class="fas fa-check text-gold mr-2"></i> Tenue : 6 à 8 mois</li>
                            </ul>
                            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20un%20RDV%20pour%20les%20Mass%C3%A9ters." target="_blank" class="btn btn-sm btn-outline-success btn-block rounded-pill font-weight-bold">
                                <i class="fab fa-whatsapp"></i> Réserver Masséters
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Section 3: Régénération Cutanée -->
            <div id="profhilo">
                <div class="d-flex align-items-center mb-4">
                    <span class="mr-3" style="width: 40px; height: 40px; background: #c5a059; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: bold;">03</span>
                    <div>
                        <h2 class="font-serif font-weight-bold text-emerald mb-0">Bio-Remodelage & Glow Cutané</h2>
                        <small class="text-muted">Hydratation en nappe, stimulation du collagène naturel et éclat intense</small>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-6 mb-4">
                        <div class="clinic-card">
                            <h4 class="font-serif font-weight-bold mb-2">Profhilo® & Skinbooster</h4>
                            <p class="text-muted">Concentré pur d'acide hyaluronique haut et bas poids moléculaire. Injecté en 5 points stratégiques pour repulper la peau, lisser les ridules et offrir un glow inimitable.</p>
                            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20pour%20le%20Profhilo." target="_blank" class="btn btn-sm btn-outline-success rounded-pill font-weight-bold">
                                <i class="fab fa-whatsapp"></i> En savoir plus sur Profhilo
                            </a>
                        </div>
                    </div>
                    <div class="col-lg-6 mb-4">
                        <div class="clinic-card">
                            <h4 class="font-serif font-weight-bold mb-2">Mésothérapie & Peelings Médicaux</h4>
                            <p class="text-muted">Cocktails vitaminés et exfoliations dermatologiques sur-mesure pour traiter les taches pigmentaires, le mélasma, resserrer les pores et illuminer le teint durablement.</p>
                            <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20pour%20un%20Peeling%20ou%20M%C3%A9soth%C3%A9rapie." target="_blank" class="btn btn-sm btn-outline-success rounded-pill font-weight-bold">
                                <i class="fab fa-whatsapp"></i> En savoir plus sur les Peelings
                            </a>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
'''
(CLINIC_DIR / "traitements.html").write_text(wrap_page("Catalogue des Traitements", "traitements", treatments_body), encoding="utf-8")
print("✅ traitements.html created!")

# ==========================================
# 4. Page: avant-apres.html (Galerie & Sliders)
# ==========================================
slider_extra_head = '''
    .ba-container {
        position: relative;
        width: 100%;
        height: 380px;
        overflow: hidden;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        user-select: none;
        border: 3px solid #c5a059;
    }
    .ba-img {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-size: cover;
        background-position: center;
    }
    .ba-before {
        border-right: 3px solid #c5a059;
        z-index: 2;
    }
    .ba-range {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        opacity: 0;
        z-index: 5;
        cursor: ew-resize;
        margin: 0;
    }
    .ba-divider {
        position: absolute;
        top: 0;
        width: 3px; height: 100%;
        background: #c5a059;
        z-index: 3;
        pointer-events: none;
        transform: translateX(-50%);
    }
    .ba-handle {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 44px; height: 44px;
        border-radius: 50%;
        background: #c5a059;
        color: #fff;
        display: flex;
        align-items: center; justify-content: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        font-size: 16px;
    }
    .ba-badge {
        position: absolute;
        bottom: 20px;
        padding: 5px 14px;
        background: rgba(15, 76, 58, 0.9);
        color: #fff;
        font-weight: 700;
        font-size: 11px;
        border-radius: 30px;
        letter-spacing: 1px;
        z-index: 4;
        border: 1px solid rgba(197, 160, 89, 0.5);
    }
    .ba-badge-left { left: 20px; }
    .ba-badge-right { right: 20px; }
'''

ba_body = '''
    <!-- Page Banner -->
    <div class="page-banner">
        <div class="container">
            <span class="badge-gold">Résultats Cliniques Documentés</span>
            <h1 class="display-4 font-weight-bold mb-3 font-serif">Galerie Avant / Après</h1>
            <p class="lead max-w-700 mx-auto" style="color: #cbd5e1; max-width: 700px; margin: 0 auto;">
                Faites glisser le curseur pour observer la subtilité, la précision et le naturel des métamorphoses réalisées par le Dr. Hanane Kashi.
            </p>
        </div>
    </div>

    <!-- Sliders Gallery -->
    <div class="py-5" style="background: #fafaf9;">
        <div class="container py-4">

            <!-- Case 1: Lèvres & Russian Lips -->
            <div class="row align-items-center mb-5 p-4 bg-white rounded shadow-sm border">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <div class="ba-container" id="ba1">
                        <div class="ba-img" style="background-image: url('assets/img/dr-kashi-procedure.jpg');"></div>
                        <div class="ba-img ba-before" id="ba1-before" style="background-image: url('assets/img/dr-kashi-results.jpg'); width: 50%;"></div>
                        <div class="ba-divider" id="ba1-divider" style="left: 50%;">
                            <div class="ba-handle"><i class="fas fa-arrows-alt-h"></i></div>
                        </div>
                        <span class="ba-badge ba-badge-left">AVANT</span>
                        <span class="ba-badge ba-badge-right">APRÈS</span>
                        <input type="range" min="0" max="100" value="50" class="ba-range" oninput="updateBA('ba1', this.value)">
                    </div>
                </div>
                <div class="col-lg-6 pl-lg-4">
                    <span class="badge px-3 py-1 text-uppercase mb-2" style="background: rgba(197,160,89,0.15); color: #c5a059; font-weight: bold;">Cas Clinique #01</span>
                    <h3 class="font-serif font-weight-bold text-emerald mb-3">Sublimation des Lèvres & Hydratation</h3>
                    <p class="text-muted" style="line-height: 1.8;">
                        Patiente de 27 ans souhaitant corriger une asymétrie de la lèvre supérieure et gagner en projection sans sur-volume. 
                        <strong>Protocole :</strong> 0.8ml d'acide hyaluronique réticulé en micro-injections avec dessin de l'arc de cupidon.
                    </p>
                    <div class="p-3 mb-3" style="background: #f8fafc; border-left: 4px solid #c5a059; border-radius: 0 10px 10px 0;">
                        <small class="text-dark font-weight-bold d-block">Observation médicale :</small>
                        <small class="text-muted">Résultat immédiatement visible, lèvres souples, projection naturelle sans aucune démarcation cutanée.</small>
                    </div>
                    <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20le%20m%C3%AAme%20r%C3%A9sultat%20que%20le%20Cas%20Clinique%20L%C3%A8vres." target="_blank" class="btn btn-sm btn-outline-success rounded-pill font-weight-bold">
                        <i class="fab fa-whatsapp"></i> Demander une consultation similaire
                    </a>
                </div>
            </div>

            <!-- Case 2: Cernes & Regard Frais -->
            <div class="row align-items-center mb-5 p-4 bg-white rounded shadow-sm border flex-lg-row-reverse">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <div class="ba-container" id="ba2">
                        <div class="ba-img" style="background-image: url('assets/img/dr-kashi-desk.png');"></div>
                        <div class="ba-img ba-before" id="ba2-before" style="background-image: url('assets/img/dr-kashi-hero-banner.jpg'); width: 50%;"></div>
                        <div class="ba-divider" id="ba2-divider" style="left: 50%;">
                            <div class="ba-handle"><i class="fas fa-arrows-alt-h"></i></div>
                        </div>
                        <span class="ba-badge ba-badge-left">AVANT</span>
                        <span class="ba-badge ba-badge-right">APRÈS</span>
                        <input type="range" min="0" max="100" value="50" class="ba-range" oninput="updateBA('ba2', this.value)">
                    </div>
                </div>
                <div class="col-lg-6 pr-lg-4">
                    <span class="badge px-3 py-1 text-uppercase mb-2" style="background: rgba(15,76,58,0.15); color: #0f4c3a; font-weight: bold;">Cas Clinique #02</span>
                    <h3 class="font-serif font-weight-bold text-emerald mb-3">Comblement Cernes Creux au Contact Osseux</h3>
                    <p class="text-muted" style="line-height: 1.8;">
                        Patiente de 38 ans souffrant d'un creux marqué donnant un air fatigué permanent malgré un sommeil suffisant.
                        <strong>Protocole :</strong> Injection douce à la micro-canule 27G au contact du périoste avec acide hyaluronique non hydrophile (Teosyal Redensity II).
                    </p>
                    <div class="p-3 mb-3" style="background: #f8fafc; border-left: 4px solid #0f4c3a; border-radius: 0 10px 10px 0;">
                        <small class="text-dark font-weight-bold d-block">Observation médicale :</small>
                        <small class="text-muted">Effacement de l'effet d'ombre, défatigage spectaculaire, aucun bleu et zéro douleur.</small>
                    </div>
                    <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20le%20m%C3%AAme%20r%C3%A9sultat%20que%20le%20Cas%20Clinique%20Cernes." target="_blank" class="btn btn-sm btn-outline-success rounded-pill font-weight-bold">
                        <i class="fab fa-whatsapp"></i> Demander une consultation similaire
                    </a>
                </div>
            </div>

            <div class="text-center py-4">
                <small class="text-muted font-italic">
                    * Tous les actes médicaux sont pratiqués par le Dr. Hanane Kashi. Les résultats peuvent varier en fonction de l'anatomie et du protocole validé lors de la consultation préalable.
                </small>
            </div>

        </div>
    </div>

    <script>
    function updateBA(id, val) {
        document.getElementById(id + '-before').style.width = val + '%';
        document.getElementById(id + '-divider').style.left = val + '%';
    }
    </script>
'''
(CLINIC_DIR / "avant-apres.html").write_text(wrap_page("Galerie Avant / Après", "avant-apres", ba_body, slider_extra_head), encoding="utf-8")
print("✅ avant-apres.html created!")

# ==========================================
# 5. Page: tarifs.html (Honoraires & Forfaits)
# ==========================================
tarifs_body = '''
    <!-- Page Banner -->
    <div class="page-banner">
        <div class="container">
            <span class="badge-gold">Transparence Médicale</span>
            <h1 class="display-4 font-weight-bold mb-3 font-serif">Honoraires & Forfaits Personnalisés</h1>
            <p class="lead max-w-700 mx-auto" style="color: #cbd5e1; max-width: 700px; margin: 0 auto;">
                Chaque patiente bénéficie d'une tarification claire, détaillée et sans surprise, incluant le suivi et la retouche de contrôle.
            </p>
        </div>
    </div>

    <!-- Pricing Cards -->
    <div class="py-5" style="background: #fafaf9;">
        <div class="container py-4">
            <div class="row">
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="clinic-card text-center">
                        <span class="badge badge-light text-uppercase px-3 py-2 border mb-3">Évaluation Initiale</span>
                        <h3 class="font-serif font-weight-bold text-emerald">Consultation Bilan</h3>
                        <div class="my-4">
                            <span class="font-weight-bold" style="font-size: 38px; color: #0f4c3a;">500</span>
                            <span class="text-muted font-weight-bold">MAD</span>
                        </div>
                        <p class="text-muted small">Diagnostic morphologique 360°, plan de traitement sur-mesure et devis précis.</p>
                        <div class="alert alert-success p-2 small mb-4" style="background: rgba(30,190,182,0.1); border-color: #1ebeb6; color: #0f4c3a;">
                            <strong>Déductible</strong> du montant de votre premier soin réalisé !
                        </div>
                        <ul class="list-unstyled small text-muted text-left mb-4">
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Examen clinique approfondi</li>
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Analyse dynamique du visage</li>
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Recommandations sans engagement</li>
                        </ul>
                        <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20une%20Consultation%20Bilan." target="_blank" class="btn btn-outline-success btn-block rounded-pill font-weight-bold">
                            <i class="fab fa-whatsapp"></i> Réserver le Bilan
                        </a>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="clinic-card text-center" style="border: 2px solid #c5a059; box-shadow: 0 15px 40px rgba(197,160,89,0.2);">
                        <span class="badge text-uppercase px-3 py-2 text-white mb-3" style="background: #c5a059;">Formule Star</span>
                        <h3 class="font-serif font-weight-bold text-emerald">Injections Visage</h3>
                        <div class="my-4">
                            <small class="text-muted font-weight-bold">À partir de</small><br>
                            <span class="font-weight-bold" style="font-size: 38px; color: #0f4c3a;">2 500</span>
                            <span class="text-muted font-weight-bold">MAD</span>
                        </div>
                        <p class="text-muted small">Acide Hyaluronique premium scellé (Juvéderm / Teoxane) ou Toxine Botulique par zone.</p>
                        <ul class="list-unstyled small text-muted text-left mb-4">
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Seringue 1ml neuve certifiée CE & FDA</li>
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Injection micro-canule indolore</li>
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Numéro de lot remis à la patiente</li>
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> <strong>Contrôle à 15 jours inclus</strong></li>
                        </ul>
                        <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20une%20séance%20d%27Injection." target="_blank" class="btn-gold btn-block justify-content-center">
                            <i class="fab fa-whatsapp"></i> Réserver ce Soin
                        </a>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="clinic-card text-center">
                        <span class="badge badge-light text-uppercase px-3 py-2 border mb-3">Harmonisation Totale</span>
                        <h3 class="font-serif font-weight-bold text-emerald">Full Face Élite</h3>
                        <div class="my-4">
                            <span class="font-weight-bold" style="font-size: 34px; color: #0f4c3a;">Sur Devis</span><br>
                            <small class="text-muted">Personnalisé selon vos besoins</small>
                        </div>
                        <p class="text-muted small">Combinaison synergique : Lissage toxine, comblement des creux et bio-remodelage Profhilo.</p>
                        <ul class="list-unstyled small text-muted text-left mb-4">
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Rajeunissement global naturel</li>
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Protocole étalé sur 1 à 2 séances</li>
                            <li class="mb-2"><i class="fas fa-check text-gold mr-2"></i> Suivi VIP prioritaire par le docteur</li>
                        </ul>
                        <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20un%20devis%20Full%20Face%20%C3%89lite." target="_blank" class="btn btn-outline-success btn-block rounded-pill font-weight-bold">
                            <i class="fab fa-whatsapp"></i> Demander un Devis
                        </a>
                    </div>
                </div>

            </div>

            <!-- Inclusions Strip -->
            <div class="p-4 bg-white rounded shadow-sm border mt-4">
                <h4 class="font-serif font-weight-bold text-emerald mb-3 text-center">Ce qui est systématiquement garanti dans chaque acte :</h4>
                <div class="row text-center">
                    <div class="col-md-3 mb-2">
                        <i class="fas fa-box-open text-gold mr-1"></i> Produit scellé devant vous
                    </div>
                    <div class="col-md-3 mb-2">
                        <i class="fas fa-certificate text-gold mr-1"></i> Traçabilité CE & FDA
                    </div>
                    <div class="col-md-3 mb-2">
                        <i class="fas fa-user-shield text-gold mr-1"></i> Aiguilles & Canules stériles
                    </div>
                    <div class="col-md-3 mb-2">
                        <i class="fas fa-calendar-check text-gold mr-1"></i> Retouche offerte à 15j
                    </div>
                </div>
            </div>

        </div>
    </div>
'''
(CLINIC_DIR / "tarifs.html").write_text(wrap_page("Honoraires & Forfaits", "tarifs", tarifs_body), encoding="utf-8")
print("✅ tarifs.html created!")

# ==========================================
# 6. Page: temoignages.html (Avis Patientes)
# ==========================================
temoignages_body = '''
    <!-- Page Banner -->
    <div class="page-banner">
        <div class="container">
            <span class="badge-gold">Témoignages & Avis Vérifiés</span>
            <h1 class="display-4 font-weight-bold mb-3 font-serif">Retours d'Expérience des Patientes</h1>
            <p class="lead max-w-700 mx-auto" style="color: #cbd5e1; max-width: 700px; margin: 0 auto;">
                Découvrez les retours authentiques de celles et ceux qui ont confié leur harmonie faciale au Dr. Hanane Kashi.
            </p>
        </div>
    </div>

    <!-- Rating Summary -->
    <div class="py-4 bg-white border-bottom">
        <div class="container text-center">
            <div class="d-inline-flex align-items-center p-3 bg-light rounded-pill border">
                <span class="font-weight-bold text-emerald mr-3" style="font-size: 26px;">4.9 / 5</span>
                <div class="text-gold mr-3">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                </div>
                <span class="text-muted small">Basé sur plus de 180 avis vérifiés de patientes à Casablanca</span>
            </div>
        </div>
    </div>

    <!-- Reviews Grid -->
    <div class="py-5" style="background: #fafaf9;">
        <div class="container py-4">
            <div class="row">
                
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="clinic-card">
                        <div class="text-gold mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <h5 class="font-serif font-weight-bold mb-2">« Regard transformé sans douleur »</h5>
                        <p class="text-muted small" style="line-height: 1.7;">
                            « J'avais une peur panique des aiguilles et des hématomes. Le Dr. Kashi a pris le temps de m'écouter et a utilisé une micro-canule. Je n'ai ressenti qu'une légère pression et mes cernes creux ont littéralement disparu. Mon entourage me dit que j'ai l'air reposée sans savoir ce que j'ai fait ! »
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div style="width: 42px; height: 42px; background: #0f4c3a; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;" class="mr-3">Z</div>
                            <div>
                                <strong class="d-block text-dark small">Zineb E.</strong>
                                <small class="text-muted">Casablanca • Comblement Cernes</small>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="clinic-card">
                        <div class="text-gold mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <h5 class="font-serif font-weight-bold mb-2">« Des lèvres tellement naturelles »</h5>
                        <p class="text-muted small" style="line-height: 1.7;">
                            « Je voulais redéfinir mes lèvres qui étaient très fines sans ressembler aux stéréotypes des réseaux sociaux. Le résultat avec le Dr. Kashi est juste sublime, élégant et parfaitement symétrique. Merci pour votre délicatesse et votre professionnalisme. »
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div style="width: 42px; height: 42px; background: #c5a059; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;" class="mr-3">M</div>
                            <div>
                                <strong class="d-block text-dark small">Meriem B.</strong>
                                <small class="text-muted">Rabat • Injections Lèvres</small>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="clinic-card">
                        <div class="text-gold mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <h5 class="font-serif font-weight-bold mb-2">« Finie la ride du lion sévère »</h5>
                        <p class="text-muted small" style="line-height: 1.7;">
                            « Mon visage avait toujours l'air sévère à cause d'une ride du lion très creusée entre les sourcils. La toxine botulique réalisée par le docteur a détendu l'ensemble sans bloquer mes sourcils. La retouche à 15 jours était impeccable. »
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div style="width: 42px; height: 42px; background: #0f4c3a; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;" class="mr-3">S</div>
                            <div>
                                <strong class="d-block text-dark small">Salma T.</strong>
                                <small class="text-muted">Casablanca • Toxine Botulique</small>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
'''
(CLINIC_DIR / "temoignages.html").write_text(wrap_page("Avis Patientes", "temoignages", temoignages_body), encoding="utf-8")
print("✅ temoignages.html created!")

# ==========================================
# 7. Page: faq.html (Questions Fréquentes)
# ==========================================
faq_body = '''
    <!-- Page Banner -->
    <div class="page-banner">
        <div class="container">
            <span class="badge-gold">Réponses Claires & Médicales</span>
            <h1 class="display-4 font-weight-bold mb-3 font-serif">Foire Aux Questions</h1>
            <p class="lead max-w-700 mx-auto" style="color: #cbd5e1; max-width: 700px; margin: 0 auto;">
                Tout ce que vous devez savoir avant votre séance d'injections ou de soins esthétiques au cabinet.
            </p>
        </div>
    </div>

    <!-- FAQ Accordions -->
    <div class="py-5" style="background: #fafaf9;">
        <div class="container py-4" style="max-width: 850px;">
            
            <div class="panel-group" id="faq-accordion" role="tablist" aria-multiselectable="true">
                
                <div class="panel panel-default clinic-card mb-3 p-3">
                    <div class="panel-heading" role="tab" id="headingOne">
                        <h4 class="panel-title font-serif">
                            <a role="button" data-toggle="collapse" data-parent="#faq-accordion" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne" class="text-emerald text-decoration-none d-flex justify-content-between align-items-center">
                                <span>1. Les injections d'acide hyaluronique sont-elles douloureuses ?</span>
                                <i class="fa fa-angle-down text-gold"></i>
                            </a>
                        </h4>
                    </div>
                    <div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">
                        <div class="panel-body text-muted small pt-3" style="line-height: 1.8;">
                            Non. Tous les acides hyaluroniques modernes utilisés par le Dr. Hanane Kashi contiennent de la lidocaïne (anesthésique local) intégrée. De plus, pour les lèvres ou les cernes, nous appliquons une crème anesthésiante 20 minutes avant le geste et privilégions la micro-canule à bout mousse, ce qui rend l'acte très confortable.
                        </div>
                    </div>
                </div>

                <div class="panel panel-default clinic-card mb-3 p-3">
                    <div class="panel-heading" role="tab" id="headingTwo">
                        <h4 class="panel-title font-serif">
                            <a class="collapsed text-emerald text-decoration-none d-flex justify-content-between align-items-center" role="button" data-toggle="collapse" data-parent="#faq-accordion" href="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                <span>2. Combien de temps durent les résultats d'une injection ?</span>
                                <i class="fa fa-angle-down text-gold"></i>
                            </a>
                        </h4>
                    </div>
                    <div id="collapseTwo" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingTwo">
                        <div class="panel-body text-muted small pt-3" style="line-height: 1.8;">
                            La durée varie selon la zone et le métabolisme individuel :<br>
                            • <strong>Lèvres :</strong> 9 à 12 mois.<br>
                            • <strong>Cernes creux :</strong> 12 à 18 mois.<br>
                            • <strong>Jawline & Pommettes :</strong> 14 à 18 mois.<br>
                            • <strong>Toxine Botulique (Botox) :</strong> 4 à 6 mois.
                        </div>
                    </div>
                </div>

                <div class="panel panel-default clinic-card mb-3 p-3">
                    <div class="panel-heading" role="tab" id="headingThree">
                        <h4 class="panel-title font-serif">
                            <a class="collapsed text-emerald text-decoration-none d-flex justify-content-between align-items-center" role="button" data-toggle="collapse" data-parent="#faq-accordion" href="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                                <span>3. Peut-on reprendre le travail immédiatement après la séance ?</span>
                                <i class="fa fa-angle-down text-gold"></i>
                            </a>
                        </h4>
                    </div>
                    <div id="collapseThree" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingThree">
                        <div class="panel-body text-muted small pt-3" style="line-height: 1.8;">
                            Absolument. Il n'y a aucune éviction sociale. De légères rougeurs ou un œdème minime peuvent apparaître sur les lèvres pendant 24 à 48 heures, mais ils sont facilement camouflables. Vous pouvez reprendre vos activités sociales dès la sortie du cabinet.
                        </div>
                    </div>
                </div>

                <div class="panel panel-default clinic-card mb-3 p-3">
                    <div class="panel-heading" role="tab" id="headingFour">
                        <h4 class="panel-title font-serif">
                            <a class="collapsed text-emerald text-decoration-none d-flex justify-content-between align-items-center" role="button" data-toggle="collapse" data-parent="#faq-accordion" href="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
                                <span>4. Quelles sont les précautions à respecter après l'acte ?</span>
                                <i class="fa fa-angle-down text-gold"></i>
                            </a>
                        </h4>
                    </div>
                    <div id="collapseFour" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingFour">
                        <div class="panel-body text-muted small pt-3" style="line-height: 1.8;">
                            Pendant les 48 heures suivant les injections, nous conseillons d'éviter le sport intensif, le sauna, le hammam et l'exposition solaire directe. Il est également recommandé de ne pas masser vigoureusement les zones injectées.
                        </div>
                    </div>
                </div>

                <div class="panel panel-default clinic-card mb-3 p-3">
                    <div class="panel-heading" role="tab" id="headingFive">
                        <h4 class="panel-title font-serif">
                            <a class="collapsed text-emerald text-decoration-none d-flex justify-content-between align-items-center" role="button" data-toggle="collapse" data-parent="#faq-accordion" href="#collapseFive" aria-expanded="false" aria-controls="collapseFive">
                                <span>5. Y a-t-il une retouche prévue après le premier traitement ?</span>
                                <i class="fa fa-angle-down text-gold"></i>
                            </a>
                        </h4>
                    </div>
                    <div id="collapseFive" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingFive">
                        <div class="panel-body text-muted small pt-3" style="line-height: 1.8;">
                            Oui. Le Dr. Hanane Kashi programme systématiquement une consultation de contrôle à 15 jours. Cette séance permet d'évaluer la parfaite intégration du produit et d'effectuer une retouche millimétrique offerte si nécessaire pour une symétrie irréprochable.
                        </div>
                    </div>
                </div>

            </div>

            <div class="text-center mt-5">
                <p class="text-muted">Vous avez une question spécifique sur votre visage ?</p>
                <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20j%27ai%20une%20question%20m%C3%A9dicale%20sp%C3%A9cifique." target="_blank" class="btn-whatsapp">
                    <i class="fab fa-whatsapp"></i> Poser votre question sur WhatsApp
                </a>
            </div>

        </div>
    </div>
'''
(CLINIC_DIR / "faq.html").write_text(wrap_page("Questions Fréquentes (FAQ)", "faq", faq_body), encoding="utf-8")
print("✅ faq.html created!")

# ==========================================
# 8. Page: contact.html (Accès & Rendez-vous)
# ==========================================
contact_body = '''
    <!-- Page Banner -->
    <div class="page-banner">
        <div class="container">
            <span class="badge-gold">Prise de Rendez-vous Privée</span>
            <h1 class="display-4 font-weight-bold mb-3 font-serif">Accès au Cabinet & Contact</h1>
            <p class="lead max-w-700 mx-auto" style="color: #cbd5e1; max-width: 700px; margin: 0 auto;">
                Notre secrétariat médical vous accueille du lundi au samedi pour planifier votre consultation avec le Dr. Hanane Kashi.
            </p>
        </div>
    </div>

    <!-- Contact Details & Form -->
    <div class="py-5" style="background: #fafaf9;">
        <div class="container py-4">
            <div class="row">
                
                <!-- Left: Info & Map -->
                <div class="col-lg-5 mb-5 mb-lg-0">
                    <div class="clinic-card mb-4">
                        <h4 class="font-serif font-weight-bold text-emerald mb-3">Coordonnées du Cabinet</h4>
                        <ul class="list-unstyled mb-4">
                            <li class="mb-3 d-flex">
                                <i class="fas fa-map-marker-alt text-gold mr-3 mt-1" style="font-size: 20px;"></i>
                                <div>
                                    <strong>Adresse :</strong><br>
                                    <span class="text-muted">Angle Boulevard d'Anfa et Rue Gauthier, Casablanca, Maroc.</span>
                                </div>
                            </li>
                            <li class="mb-3 d-flex">
                                <i class="fas fa-phone-alt text-gold mr-3 mt-1" style="font-size: 20px;"></i>
                                <div>
                                    <strong>Téléphone Secrétariat :</strong><br>
                                    <a href="tel:+212600980685" class="text-emerald font-weight-bold">+212 600 980 685</a>
                                </div>
                            </li>
                            <li class="mb-3 d-flex">
                                <i class="fab fa-whatsapp text-success mr-3 mt-1" style="font-size: 22px;"></i>
                                <div>
                                    <strong>WhatsApp Prioritaire :</strong><br>
                                    <a href="https://wa.me/212600980685" target="_blank" class="text-success font-weight-bold">+212 600 980 685 (Réponse en 15 min)</a>
                                </div>
                            </li>
                            <li class="mb-3 d-flex">
                                <i class="fas fa-clock text-gold mr-3 mt-1" style="font-size: 20px;"></i>
                                <div>
                                    <strong>Horaires d'Ouverture :</strong><br>
                                    <span class="text-muted">Lundi - Vendredi : 09h00 - 19h00<br>Samedi : 09h00 - 14h00</span>
                                </div>
                            </li>
                        </ul>
                        <div class="p-3 bg-light rounded border text-center">
                            <i class="fas fa-parking text-gold mr-2"></i>
                            <small class="text-muted">Parking surveillé disponible à proximité immédiate.</small>
                        </div>
                    </div>
                </div>

                <!-- Right: Booking Form with CRM Storage -->
                <div class="col-lg-7">
                    <div class="clinic-card p-4 p-md-5">
                        <h3 class="font-serif font-weight-bold text-emerald mb-2">Demande de Consultation</h3>
                        <p class="text-muted small mb-4">Remplissez ce formulaire pour être recontactée immédiatement par notre secrétaire médicale.</p>

                        <form id="contactBookingForm" onsubmit="handleContactPageSubmit(event)">
                            <div class="form-group mb-3">
                                <label class="font-weight-bold small text-dark">Nom et Prénom *</label>
                                <input type="text" id="cpName" class="form-control rounded-pill" placeholder="Ex: Salma Berrada" required>
                            </div>

                            <div class="row">
                                <div class="col-md-6 form-group mb-3">
                                    <label class="font-weight-bold small text-dark">Numéro de Téléphone / WhatsApp *</label>
                                    <input type="tel" id="cpPhone" class="form-control rounded-pill" placeholder="Ex: 06 12 34 56 78" required>
                                </div>
                                <div class="col-md-6 form-group mb-3">
                                    <label class="font-weight-bold small text-dark">Traitement Souhaité *</label>
                                    <select id="cpTreatment" class="form-control rounded-pill" required>
                                        <option value="Consultation Bilan Visage">Consultation Bilan Visage (500 MAD)</option>
                                        <option value="Injections Lèvres & Russian Lips">Injections Lèvres & Russian Lips</option>
                                        <option value="Comblement Cernes Creux">Comblement Cernes Creux</option>
                                        <option value="Toxine Botulique (Botox)">Toxine Botulique (Botox)</option>
                                        <option value="Jawline & Menton">Jawline & Menton</option>
                                        <option value="Profhilo & Skinbooster">Profhilo & Skinbooster Glow</option>
                                        <option value="Autre demande">Autre soin spécifique</option>
                                    </select>
                                </div>
                            </div>

                            <div class="form-group mb-3">
                                <label class="font-weight-bold small text-dark">Date Préférée (Optionnel)</label>
                                <input type="date" id="cpDate" class="form-control rounded-pill">
                            </div>

                            <div class="form-group mb-4">
                                <label class="font-weight-bold small text-dark">Précisions ou remarques</label>
                                <textarea id="cpNote" class="form-control" rows="3" placeholder="Indiquez vos disponibilités ou vos questions éventuelles..." style="border-radius: 15px;"></textarea>
                            </div>

                            <button type="submit" class="btn-gold btn-block justify-content-center py-3">
                                <i class="fas fa-paper-plane mr-2"></i> Envoyer ma Demande de Rendez-vous
                            </button>
                            <small class="text-muted d-block text-center mt-3">
                                Vos données médicales restent strictement confidentielles et enregistrées de manière sécurisée.
                            </small>
                        </form>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <script>
    function handleContactPageSubmit(e) {
        e.preventDefault();
        var name = document.getElementById('cpName').value.trim();
        var phone = document.getElementById('cpPhone').value.trim();
        var treatment = document.getElementById('cpTreatment').value;
        var date = document.getElementById('cpDate').value;
        var note = document.getElementById('cpNote').value.trim();

        // 1. Record into CRM
        recordPatientInCRM(name, phone, treatment, date, 'Page Contact', note);

        // 2. Open WhatsApp confirmation
        var msg = "Bonjour Dr. Hanane Kashi,%0A%0AJe souhaite réserver une consultation :%0A" +
                  "• Nom : " + encodeURIComponent(name) + "%0A" +
                  "• Téléphone : " + encodeURIComponent(phone) + "%0A" +
                  "• Soin souhaité : " + encodeURIComponent(treatment);
        if (date) {
            msg += "%0A• Date souhaitée : " + encodeURIComponent(date);
        }
        if (note) {
            msg += "%0A• Remarque : " + encodeURIComponent(note);
        }
        msg += "%0A%0AMerci de me recontacter pour confirmer le créneau.";

        window.open("https://wa.me/212600980685?text=" + msg, "_blank");
    }
    </script>
'''
(CLINIC_DIR / "contact.html").write_text(wrap_page("Contact & Prise de Rendez-vous", "contact", contact_body), encoding="utf-8")
print("✅ contact.html created!")

print("\n🚀 All Dr. Hanane Kashi pages successfully built and linked!")
