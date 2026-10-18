# -*- coding: utf-8 -*-
"""
Finalizes Dr. Hanane Kashi Aesthetic Clinic for 100% Production Readiness:
1. Archives all leftover template files (Healdi template pages with Lorem Ipsum)
2. Builds branded 404.html
3. Adds Open Graph, Twitter Cards, SEO & Schema.org JSON-LD to all active pages
4. Adds Arabic multi-page navigation to ar.html
5. Adds CSV/Excel export to admin.html (CRM)
6. Generates sitemap.xml and robots.txt (protects admin.html from crawling)
7. Mirrors everything to Desktop
"""

import sys, os, shutil, re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CLINIC_DIR = Path(r"C:\Users\USER\.gemini\antigravity\scratch\dr-hanane-kashi-clinic")
DESKTOP_DIR = Path(r"C:\Users\USER\Desktop\dr-hanane-kashi-clinic")

print("=== STARTING DR. HANANE KASHI PRODUCTION FINALIZATION ===")

# ----------------------------------------------------
# 1. Archive Leftover Template Files
# ----------------------------------------------------
archive_dir = CLINIC_DIR / "_template_archive"
archive_dir.mkdir(exist_ok=True)

template_junk = [
    "about-us.html",
    "blog-2-colum.html",
    "blog-3-colum.html",
    "blog-single-with-sidebar.html",
    "blog-single.html",
    "blog-standard.html",
    "blog-with-sidebar.html",
    "department-single.html",
    "departments-2.html",
    "departments-3.html",
    "departments-4.html",
    "departments.html",
    "doctors-2.html",
    "doctors.html",
    "gallery.html",
    "index-2.html",
    "index-3.html",
    "index-4.html",
    "index-5.html"
]

archived_count = 0
for fname in template_junk:
    fpath = CLINIC_DIR / fname
    if fpath.exists():
        shutil.move(str(fpath), str(archive_dir / fname))
        archived_count += 1

print(f"📦 Archived {archived_count} leftover template demo files to _template_archive/.")

# ----------------------------------------------------
# 2. Branded 404 Page (404.html)
# ----------------------------------------------------
page_404_html = '''<!DOCTYPE html>
<html lang="fr" dir="ltr">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Page Non Trouvée (404) | Dr. Hanane Kashi Casablanca</title>
    <link rel="shortcut icon" href="assets/img/dr-kashi-logo.jpg" type="image/x-icon">

    <!-- CSS Assets -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />
    <link href="assets/css/font-awesome.min.css" rel="stylesheet" />
    <link href="style.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: linear-gradient(135deg, #09261d 0%, #0f4c3a 100%);
            color: #fff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
        }
        .font-serif { font-family: 'Playfair Display', serif; }
        .box-404 {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(197, 160, 89, 0.3);
            border-radius: 24px;
            padding: 50px 30px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        }
        .code-404 {
            font-size: 90px;
            font-weight: 800;
            color: #c5a059;
            line-height: 1;
            margin-bottom: 15px;
            letter-spacing: -2px;
        }
        .btn-gold {
            background: linear-gradient(135deg, #d4af37, #c5a059);
            color: #fff !important;
            padding: 12px 28px;
            border-radius: 50px;
            font-weight: 700;
            text-decoration: none;
            display: inline-block;
            margin: 6px;
            box-shadow: 0 10px 25px rgba(197,160,89,0.4);
            transition: all 0.3s ease;
        }
        .btn-gold:hover { transform: translateY(-2px); }
        .btn-outline {
            border: 1px solid rgba(255,255,255,0.4);
            color: #fff !important;
            padding: 12px 28px;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            margin: 6px;
            transition: all 0.3s ease;
        }
        .btn-outline:hover { background: rgba(255,255,255,0.1); }
    </style>
</head>
<body>
    <div class="box-404">
        <img src="assets/img/dr-kashi-logo.jpg" alt="Logo Dr Kashi" style="width: 70px; height: 70px; border-radius: 50%; border: 2px solid #c5a059; margin-bottom: 20px;">
        <div class="code-404 font-serif">404</div>
        <h2 class="font-serif mb-3">Page Non Trouvée</h2>
        <p class="text-light opacity-75 mb-4" style="color: #cbd5e1; font-size: 15px; line-height: 1.6;">
            La page que vous recherchez semble introuvable ou a été déplacée. Vous pouvez retourner à l'accueil ou explorer notre catalogue de soins esthétiques.
        </p>
        <div>
            <a href="index.html" class="btn-gold"><i class="fa fa-home mr-1"></i> Retour à l'Accueil</a>
            <a href="traitements.html" class="btn-outline"><i class="fa fa-magic mr-1"></i> Nos Traitements</a>
            <a href="https://wa.me/212600980685" target="_blank" class="btn-outline" style="border-color: #25D366; color: #25D366 !important;"><i class="fa fa-whatsapp mr-1"></i> WhatsApp</a>
        </div>
    </div>
</body>
</html>'''
(CLINIC_DIR / "404.html").write_text(page_404_html, encoding="utf-8")
print("✅ Branded 404.html created!")

# ----------------------------------------------------
# 3. Add Open Graph, SEO, and Schema.org JSON-LD to Active Pages
# ----------------------------------------------------
SCHEMA_JSON_LD = '''
    <!-- Schema.org MedicalBusiness JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Physician",
      "name": "Docteur Hanane Kashi - Médecine Esthétique & Laser",
      "image": "assets/img/dr-kashi-desk.png",
      "url": "https://drhananekashi.ma",
      "telephone": "+212600980685",
      "priceRange": "500 - 5000 MAD",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Angle Boulevard d'Anfa et Rue Gauthier",
        "addressLocality": "Casablanca",
        "addressRegion": "Grand Casablanca",
        "postalCode": "20000",
        "addressCountry": "MA"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 33.589886,
        "longitude": -7.632053
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "09:00",
          "closes": "19:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Saturday"],
          "opens": "09:00",
          "closes": "14:00"
        }
      ],
      "medicalSpecialty": [
        "Dermatology",
        "PlasticSurgery"
      ]
    }
    </script>
'''

pages_meta = {
    "index.html": {
        "title": "Docteur Hanane Kashi | Médecine Esthétique & Anti-Âge Casablanca",
        "desc": "Cabinet de médecine esthétique à Casablanca par le Dr. Hanane Kashi. Injections d'acide hyaluronique, toxine botulique (botox), comblement cernes, jawline. Sublimer sans figer.",
        "og_title": "Dr. Hanane Kashi | Médecine Esthétique & Anti-Âge Casablanca"
    },
    "a-propos.html": {
        "title": "Le Cabinet & Dr. Hanane Kashi | Médecine Esthétique Casablanca",
        "desc": "Découvrez le parcours du Dr. Hanane Kashi, formée à Paris et Casablanca, ainsi que la philosophie d'excellence et les normes de sécurité du cabinet.",
        "og_title": "Le Cabinet & Le Dr. Hanane Kashi | Expertise & Éthique"
    },
    "traitements.html": {
        "title": "Catalogue des Traitements & Soins | Dr. Hanane Kashi Casablanca",
        "desc": "Guide complet des actes esthétiques : acide hyaluronique lèvres & cernes, toxine botulique, skinbooster Profhilo, peelings et régénération cutanée.",
        "og_title": "Catalogue des Soins Esthétiques | Dr. Hanane Kashi"
    },
    "avant-apres.html": {
        "title": "Galerie Avant / Après Interactive | Dr. Hanane Kashi Casablanca",
        "desc": "Observez les résultats réels et naturels obtenus par le Dr. Hanane Kashi grâce aux curseurs interactifs Avant/Après.",
        "og_title": "Galerie Avant / Après | Résultats Naturels & Cliniques"
    },
    "tarifs.html": {
        "title": "Honoraires & Forfaits Personnalisés | Dr. Hanane Kashi Casablanca",
        "desc": "Tarification transparente des actes esthétiques à Casablanca. Injections dès 2 500 MAD, consultation diagnostic déductible, retouche à 15 jours offerte.",
        "og_title": "Honoraires & Tarifs Transparents | Dr. Hanane Kashi"
    },
    "temoignages.html": {
        "title": "Avis & Témoignages Patientes | Dr. Hanane Kashi Casablanca",
        "desc": "Note 4.9/5 basée sur plus de 180 avis de patientes à Casablanca. Témoignages vérifiés sur la douceur du geste et le naturel des résultats.",
        "og_title": "Avis & Retours d'Expérience Patientes | Note 4.9/5"
    },
    "faq.html": {
        "title": "Foire Aux Questions (FAQ) | Dr. Hanane Kashi Casablanca",
        "desc": "Réponses médicales à toutes vos interrogations : douleur, durée de tenue, précautions post-injection et contre-indications.",
        "og_title": "Questions Fréquentes sur les Injections | Dr. Hanane Kashi"
    },
    "contact.html": {
        "title": "Accès au Cabinet & Rendez-vous | Dr. Hanane Kashi Casablanca",
        "desc": "Prenez rendez-vous directement en ligne ou sur WhatsApp avec le Dr. Hanane Kashi au Quartier Gauthier, Casablanca.",
        "og_title": "Contact & Prise de Rendez-vous | Cabinet Dr. Hanane Kashi"
    }
}

for fname, meta in pages_meta.items():
    fpath = CLINIC_DIR / fname
    if not fpath.exists():
        continue
    c = fpath.read_text(encoding="utf-8")
    
    # Check if OG tags already present
    if 'property="og:title"' not in c:
        og_block = f'''
    <!-- Open Graph / Facebook / WhatsApp Preview -->
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Cabinet Dr. Hanane Kashi">
    <meta property="og:title" content="{meta['og_title']}">
    <meta property="og:description" content="{meta['desc']}">
    <meta property="og:image" content="assets/img/dr-kashi-hero-banner.jpg">
    <meta property="og:locale" content="fr_FR">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{meta['og_title']}">
    <meta name="twitter:description" content="{meta['desc']}">
    <meta name="twitter:image" content="assets/img/dr-kashi-hero-banner.jpg">
    <meta name="theme-color" content="#0f4c3a">
    {SCHEMA_JSON_LD}
'''
        c = c.replace('</head>', f'{og_block}\n</head>')
        fpath.write_text(c, encoding="utf-8")
        print(f"✅ Enhanced SEO, Open Graph & Schema.org in {fname}")

# ----------------------------------------------------
# 4. Update ar.html with Multi-page Pages Dropdown
# ----------------------------------------------------
ar_path = CLINIC_DIR / "ar.html"
if ar_path.exists():
    ar_c = ar_path.read_text(encoding="utf-8")
    
    # Arabic dropdown
    ar_dropdown = '''
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span style="color: #c5a059; font-weight: 700;">صفحات</span> <i class="fa fa-angle-down"></i></a>
                            <ul class="dropdown-menu">
                                <li><a href="a-propos.html"><i class="fa fa-user-md ml-2" style="color: #c5a059;"></i> العيادة والدكتورة كاشي</a></li>
                                <li><a href="traitements.html"><i class="fa fa-magic ml-2" style="color: #c5a059;"></i> قائمة العلاجات</a></li>
                                <li><a href="avant-apres.html"><i class="fa fa-sliders ml-2" style="color: #c5a059;"></i> معرض قبل / بعد</a></li>
                                <li><a href="tarifs.html"><i class="fa fa-tag ml-2" style="color: #c5a059;"></i> لائحة الأسعار</a></li>
                                <li><a href="temoignages.html"><i class="fa fa-star ml-2" style="color: #c5a059;"></i> آراء المريضات</a></li>
                                <li><a href="faq.html"><i class="fa fa-question-circle ml-2" style="color: #c5a059;"></i> الأسئلة الشائعة</a></li>
                                <li><a href="contact.html"><i class="fa fa-map-marker ml-2" style="color: #c5a059;"></i> التواصل والعنوان</a></li>
                                <li class="divider"></li>
                                <li><a href="admin.html"><i class="fa fa-lock ml-2" style="color: #0f4c3a;"></i> إدارة المواعيد (CRM)</a></li>
                            </ul>
                        </li>
    '''
    # Insert before the appointment button in ar.html navbar
    if 'صفحات' not in ar_c:
        ar_c = ar_c.replace('<li><a href="#contact">تواصل معنا</a></li>', f'<li><a href="contact.html">تواصل معنا</a></li>\n{ar_dropdown}')
        ar_path.write_text(ar_c, encoding="utf-8")
        print("✅ Added Arabic pages dropdown to ar.html")

# ----------------------------------------------------
# 5. Add CSV Export & Backup in admin.html (CRM)
# ----------------------------------------------------
admin_path = CLINIC_DIR / "admin.html"
if admin_path.exists():
    admin_c = admin_path.read_text(encoding="utf-8")
    
    # Add export button to admin header
    if 'exportToCSV' not in admin_c:
        btn_code = '''
            <button onclick="exportToCSV()" class="btn btn-sm btn-outline-warning ml-2 font-weight-bold" style="border-radius: 8px;">
                <i class="fa fa-file-excel-o mr-1"></i> Exporter CSV
            </button>
            <button onclick="clearAllDataPrompt()" class="btn btn-sm btn-outline-danger ml-2 font-weight-bold" style="border-radius: 8px;">
                <i class="fa fa-trash mr-1"></i> Réinitialiser
            </button>
        '''
        admin_c = admin_c.replace('<button class="btn btn-gold font-weight-bold" data-toggle="modal" data-target="#newPatientModal">',
                                  f'{btn_code}\n<button class="btn btn-gold font-weight-bold" data-toggle="modal" data-target="#newPatientModal">')
        
        # Add JS functions
        js_functions = '''
        function exportToCSV() {
            if (!patients || patients.length === 0) {
                alert("Aucune donnée de patiente à exporter.");
                return;
            }
            let csv = "\\uFEFF"; // UTF-8 BOM for Excel
            csv += "ID;Nom;Telephone;Traitement;Date;Statut;Source;Remarque\\n";
            patients.forEach(p => {
                const row = [
                    p.id || '',
                    (p.name || '').replace(/;/g, ' '),
                    (p.phone || '').replace(/;/g, ' '),
                    (p.treatment || '').replace(/;/g, ' '),
                    p.date || '',
                    p.status || '',
                    p.source || 'Site Web',
                    (p.note || '').replace(/;/g, ' ').replace(/\\n/g, ' ')
                ];
                csv += row.join(';') + "\\n";
            });
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = "patientes_dr_hanane_kashi_" + new Date().toISOString().slice(0, 10) + ".csv";
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }

        function clearAllDataPrompt() {
            if (confirm("Attention : Voulez-vous vraiment réinitialiser la base locale et recharger les données de démonstration ?")) {
                localStorage.removeItem('dr_kashi_patients');
                loadPatients();
            }
        }
        '''
        admin_c = admin_c.replace('</script>', f'{js_functions}\n</script>')
        admin_path.write_text(admin_c, encoding="utf-8")
        print("✅ Added 1-Click Excel/CSV Export and Reset features to admin.html CRM")

# ----------------------------------------------------
# 6. Generate robots.txt and sitemap.xml
# ----------------------------------------------------
sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://drhananekashi.ma/</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://drhananekashi.ma/a-propos.html</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://drhananekashi.ma/traitements.html</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://drhananekashi.ma/avant-apres.html</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://drhananekashi.ma/tarifs.html</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://drhananekashi.ma/temoignages.html</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://drhananekashi.ma/faq.html</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://drhananekashi.ma/contact.html</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://drhananekashi.ma/ar.html</loc>
    <lastmod>2026-10-18</lastmod>
    <priority>0.9</priority>
  </url>
</urlset>'''

(CLINIC_DIR / "sitemap.xml").write_text(sitemap_xml, encoding="utf-8")
print("✅ sitemap.xml created!")

robots_txt = '''User-agent: *
Allow: /
Disallow: /admin.html
Disallow: /_template_archive/

Sitemap: https://drhananekashi.ma/sitemap.xml
'''
(CLINIC_DIR / "robots.txt").write_text(robots_txt, encoding="utf-8")
print("✅ robots.txt created (protects admin.html CRM from search engines)!")

# ----------------------------------------------------
# 7. Mirror to Desktop
# ----------------------------------------------------
DESKTOP_DIR.mkdir(parents=True, exist_ok=True)
for item in CLINIC_DIR.iterdir():
    if item.name.startswith('.'): continue
    d = DESKTOP_DIR / item.name
    if item.is_dir():
        if not d.exists():
            shutil.copytree(item, d)
    else:
        shutil.copy2(item, d)

print("🚀 Successfully mirrored Dr. Hanane Kashi production files to Desktop!")
print("=== DR. HANANE KASHI CLINIC IS NOW 100% PRODUCTION READY ===")
