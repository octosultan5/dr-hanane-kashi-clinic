# -*- coding: utf-8 -*-
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CLINIC_DIR = Path(r"C:\Users\USER\.gemini\antigravity\scratch\dr-hanane-kashi-clinic")

def get_head(title, desc, is_rtl=False):
    rtl_style = """
        body { direction: rtl; text-align: right; }
        .text-left { text-align: right !important; }
        .text-right { text-align: left !important; }
        .mr-1, .mr-2, .mr-3 { margin-left: 0.5rem !important; margin-right: 0 !important; }
        .ml-1, .ml-2, .ml-3 { margin-right: 0.5rem !important; margin-left: 0 !important; }
        .testimonial-quote-box { border-left: none !important; border-right: 5px solid var(--primary-gold) !important; border-radius: 20px 0 0 20px !important; }
        .navbar-nav { float: left !important; }
        .navbar-brand { float: right !important; }
    """ if is_rtl else ""

    return f"""<!DOCTYPE html>
<html lang="{"ar" if is_rtl else "fr"}" dir="{"rtl" if is_rtl else "ltr"}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{desc}">
    <title>{title}</title>
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
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Cairo:wght@400;600;700;800&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">

    <style>
        :root {{
            --primary-emerald: #0f4c3a;
            --primary-gold: #c5a059;
            --primary-accent: #1ebeb6;
            --text-dark: #1e293b;
        }}
        body {{
            font-family: {"'Tajawal', 'Cairo', sans-serif" if is_rtl else "'Plus Jakarta Sans', sans-serif"};
            color: #334155;
            background-color: #ffffff;
        }}
        h1, h2, h3, .font-serif {{
            font-family: {"'Tajawal', 'Cairo', sans-serif" if is_rtl else "'Playfair Display', serif"};
        }}
        .bg-emerald {{
            background-color: var(--primary-emerald) !important;
        }}
        .text-emerald {{
            color: var(--primary-emerald) !important;
        }}
        .text-gold {{
            color: var(--primary-gold) !important;
        }}
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
        }}
        .btn-gold:hover {{
            transform: translateY(-2px);
            box-shadow: 0 15px 30px rgba(197, 160, 89, 0.6);
            color: #fff;
        }}
        .btn-whatsapp {{
            background: #25D366;
            color: #fff !important;
            padding: 13px 26px;
            font-weight: 700;
            border-radius: 50px;
            box-shadow: 0 10px 25px rgba(37, 211, 102, 0.35);
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }}
        .btn-whatsapp:hover {{
            background: #20ba5a;
            transform: translateY(-2px);
            color: #fff;
        }}
        .floating-whatsapp {{
            position: fixed;
            bottom: 85px;
            right: 25px;
            background: #25D366;
            color: #fff !important;
            width: 62px;
            height: 62px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            box-shadow: 0 8px 30px rgba(37, 211, 102, 0.6);
            z-index: 9999;
            transition: transform 0.3s ease;
            animation: pulse-green 2s infinite;
        }}
        .floating-whatsapp:hover {{
            transform: scale(1.1);
        }}
        @keyframes pulse-green {{
            0% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }}
            70% {{ box-shadow: 0 0 0 18px rgba(37, 211, 102, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }}
        }}
        .sticky-mobile-bar {{
            position: fixed;
            bottom: 0;
            left: 0;
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
        .sticky-call {{
            background: #ffffff;
            color: #0f4c3a !important;
        }}
        .sticky-wa {{
            background: #25D366;
            color: #ffffff !important;
        }}
        @media (min-width: 992px) {{
            .sticky-mobile-bar {{
                display: none;
            }}
            .floating-whatsapp {{
                bottom: 30px;
            }}
        }}
        .hero-aesthetic {{
            background: linear-gradient(135deg, rgba(15, 76, 58, 0.93) 0%, rgba(10, 45, 35, 0.96) 100%), url('assets/img/dr-kashi-hero-banner.jpg') center/cover no-repeat;
            padding: 140px 0 110px;
            color: #fff;
            position: relative;
        }}
        .doctor-badge-card {{
            background: #ffffff;
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 20px 45px rgba(15, 76, 58, 0.12);
            border: 1px solid rgba(197, 160, 89, 0.25);
        }}
        .treatment-card {{
            background: #fff;
            border-radius: 20px;
            padding: 30px 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            transition: all 0.3s ease;
            border: 1px solid #f1f5f9;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .treatment-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(15, 76, 58, 0.12);
            border-color: var(--primary-gold);
        }}
        .testimonial-quote-box {{
            background: #f8fafc;
            border-left: 5px solid var(--primary-gold);
            padding: 25px;
            border-radius: 0 20px 20px 0;
            margin: 20px 0;
        }}
        .lang-switch-btn {{
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #fff;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        .lang-switch-btn:hover {{
            background: #c5a059;
            color: #fff;
            border-color: #c5a059;
        }}
        {rtl_style}
    </style>
</head>
"""

def generate_french_page():
    head = get_head(
        title="Docteur Hanane Kashi | Médecine Esthétique & Anti-Âge à Casablanca",
        desc="Sublimer sans figer, harmoniser sans transformer. Injections d'acide hyaluronique, botox, vallée des larmes, pommettes, profiloplastie à Casablanca.",
        is_rtl=False
    )

    body = """<body>
    <!-- Top Bar -->
    <div class="top-bar-area bg-emerald text-light py-2" style="border-bottom: 1px solid rgba(255,255,255,0.1);">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 col-12 text-center text-lg-left mb-2 mb-lg-0">
                    <span style="font-size: 13px;">
                        <i class="fas fa-map-marker-alt text-gold mr-1"></i> Cabinet de Médecine Esthétique — Casablanca, Maroc
                    </span>
                </div>
                <div class="col-lg-6 col-12 text-center text-lg-right d-flex justify-content-center justify-content-lg-end align-items-center">
                    <a href="tel:0520604484" class="text-light mr-3 font-weight-bold" style="font-size: 13px;">
                        <i class="fas fa-phone-alt text-gold mr-1"></i> 05 20 60 44 84
                    </a>
                    <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20prendre%20un%20rendez-vous." target="_blank" class="text-light font-weight-bold mr-3" style="font-size: 13px;">
                        <i class="fab fa-whatsapp text-success mr-1"></i> 06 00 98 06 85
                    </a>
                    <!-- Language Switcher -->
                    <a href="ar.html" class="lang-switch-btn ml-2">
                        🇲🇦 العربية
                    </a>
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
                        <img src="assets/img/dr-kashi-logo.jpg" alt="Logo Dr Hanane Kashi" style="height: 52px; width: 52px; border-radius: 50%; object-fit: cover; border: 2px solid #c5a059;" class="mr-2">
                        <div style="line-height: 1.2;">
                            <span class="font-serif font-weight-bold" style="font-size: 22px; color: var(--primary-emerald); letter-spacing: -0.5px;">Dr. Hanane Kashi</span>
                            <span class="d-block text-muted" style="font-size: 10px; text-transform: uppercase; letter-spacing: 2px;">Médecine Esthétique & Laser</span>
                        </div>
                    </a>
                </div>

                <div class="collapse navbar-collapse" id="navbar-menu">
                    <ul class="nav navbar-nav navbar-right" data-in="fadeInDown" data-out="fadeOutUp">
                        <li><a href="#home">Accueil</a></li>
                        <li><a href="#docteur">Le Docteur</a></li>
                        <li><a href="#traitements">Traitements</a></li>
                        <li><a href="#cas-pratique">Avant / Après</a></li>
                        <li><a href="#temoignages">Témoignages</a></li>
                        <li><a href="#contact">Contact</a></li>
                        <li class="d-none d-lg-block ml-3">
                            <a href="#rendez-vous" class="btn-gold" style="padding: 8px 22px !important; margin-top: 18px; color: #fff !important; font-size: 13px;">Prendre RDV</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <div class="hero-aesthetic">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-7">
                    <span class="badge px-3 py-2 text-uppercase mb-3" style="background: rgba(197, 160, 89, 0.25); color: #fce7b2; border: 1px solid #c5a059; font-size: 12px; letter-spacing: 1.5px; border-radius: 30px;">
                        ✨ Médecine Esthétique Haute Précision à Casablanca
                    </span>
                    <h1 class="display-4 font-weight-bold mb-3" style="line-height: 1.2; text-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                        Sublimer sans figer, <br>
                        <span class="text-gold" style="font-style: italic;">harmoniser sans transformer.</span>
                    </h1>
                    <p class="lead mb-4" style="color: #e2e8f0; font-size: 18px; max-width: 600px;">
                        Chaque visage possède sa propre harmonie. Le Dr. Hanane Kashi réalise des protocoles d'injections sur-mesure pour restaurer les volumes, défatiguer le regard et sublimer vos traits avec une discrétion absolue.
                    </p>
                    <div class="d-flex flex-wrap gap-3">
                        <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20une%20consultation%20d'%C3%A9valuation." target="_blank" class="btn-whatsapp mr-3 mb-2">
                            <i class="fab fa-whatsapp" style="font-size: 20px;"></i> Réserver sur WhatsApp
                        </a>
                        <a href="#traitements" class="btn btn-outline-light mb-2 font-weight-bold" style="border-radius: 50px; padding: 13px 26px;">
                            Découvrir les Traitements
                        </a>
                    </div>
                </div>
                <div class="col-lg-5 mt-5 mt-lg-0 text-center">
                    <div class="doctor-badge-card text-dark position-relative mx-auto" style="max-width: 380px;">
                        <div class="overflow-hidden rounded-circle mx-auto mb-3" style="width: 220px; height: 220px; border: 5px solid #c5a059; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
                            <img src="assets/img/dr-hanane-kashi.jpg" alt="Dr Hanane Kashi" class="img-fluid w-100 h-100" style="object-fit: cover;">
                        </div>
                        <h4 class="font-serif font-weight-bold mb-1" style="color: var(--primary-emerald);">Docteur Hanane Kashi</h4>
                        <p class="text-muted mb-2 font-weight-bold" style="font-size: 13px;">Médecin Esthétique & Anti-Âge</p>
                        <p class="small text-muted mb-3" style="line-height: 1.4;">Casablanca • Approche naturelle • Produits certifiés CE & FDA</p>
                        <div class="border-top pt-3 d-flex justify-content-around text-center">
                            <div>
                                <strong class="d-block text-emerald font-weight-bold" style="font-size: 18px;">100%</strong>
                                <span class="text-muted small">Sur-Mesure</span>
                            </div>
                            <div>
                                <strong class="d-block text-emerald font-weight-bold" style="font-size: 18px;">Naturel</strong>
                                <span class="text-muted small">Sans Effet Figé</span>
                            </div>
                            <div>
                                <strong class="d-block text-emerald font-weight-bold" style="font-size: 18px;">Doux</strong>
                                <span class="text-muted small">Micro-Canule</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Trust Strip -->
    <div class="py-4" style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="row text-center">
                <div class="col-md-4 col-12 mb-3 mb-md-0">
                    <div class="d-flex align-items-center justify-content-center">
                        <i class="fas fa-certificate text-gold mr-3" style="font-size: 28px;"></i>
                        <div class="text-left">
                            <h6 class="mb-0 font-weight-bold text-dark">Produits Certifiés CE & FDA</h6>
                            <small class="text-muted">Acide hyaluronique et toxines premium</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 col-12 mb-3 mb-md-0">
                    <div class="d-flex align-items-center justify-content-center">
                        <i class="fas fa-feather-alt text-emerald mr-3" style="font-size: 28px;"></i>
                        <div class="text-left">
                            <h6 class="mb-0 font-weight-bold text-dark">Résultat Subtil & Discret</h6>
                            <small class="text-muted">"Sublimer sans figer votre expression"</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="d-flex align-items-center justify-content-center">
                        <i class="fas fa-heart text-danger mr-3" style="font-size: 28px;"></i>
                        <div class="text-left">
                            <h6 class="mb-0 font-weight-bold text-dark">Écoute & Confort Patient</h6>
                            <small class="text-muted">Analyse morphologique personnalisée</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- About Section -->
    <section id="docteur" class="py-5" style="background: #ffffff;">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0 text-center">
                    <div class="position-relative d-inline-block">
                        <img src="assets/img/dr-kashi-cabinet-wall.jpg" alt="Cabinet Dr Hanane Kashi avec Logo Mural Doré" class="img-fluid rounded-lg shadow-lg" style="max-height: 460px; object-fit: cover; border: 4px solid #fff;">
                        <div class="position-absolute p-3 rounded-lg bg-emerald text-light text-left shadow" style="bottom: -20px; right: -15px; max-width: 260px;">
                            <span class="d-block text-gold font-weight-bold" style="font-size: 13px;">Méthode Dr. Kashi</span>
                            <small style="font-size: 12px; line-height: 1.3;">Un protocole précis qui respecte l'ossature et les volumes naturels du visage.</small>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 pl-lg-5">
                    <span class="text-uppercase text-gold font-weight-bold" style="font-size: 13px; letter-spacing: 2px;">Philosophie & Savoir-Faire</span>
                    <h2 class="display-5 font-serif font-weight-bold mt-2 mb-3" style="color: var(--primary-emerald);">
                        L'art de révéler votre beauté sans la dénaturer
                    </h2>
                    <p class="text-muted" style="line-height: 1.7;">
                        En médecine esthétique, le plus grand secret d'une intervention réussie est que personne ne devine ce que vous avez fait, mais que tout le monde remarque votre bonne mine.
                    </p>
                    <p class="text-muted" style="line-height: 1.7;">
                        Au cabinet du Dr. Hanane Kashi à Casablanca, nous privilégions la <strong>micro-nutrition des volumes</strong> et la <strong>technique à la micro-canule souple</strong>. Cela permet un travail indolore, sans bleus, et avec une reprise immédiate de vos activités quotidiennes.
                    </p>
                    <div class="row mt-4">
                        <div class="col-sm-6 mb-3">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-emerald mr-2" style="font-size: 20px;"></i>
                                <span class="font-weight-bold text-dark">Diagnostic complet visage</span>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-emerald mr-2" style="font-size: 20px;"></i>
                                <span class="font-weight-bold text-dark">Zéro effet artificiel</span>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-emerald mr-2" style="font-size: 20px;"></i>
                                <span class="font-weight-bold text-dark">Injections personnalisées</span>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-emerald mr-2" style="font-size: 20px;"></i>
                                <span class="font-weight-bold text-dark">Suivi médical dédié</span>
                            </div>
                        </div>
                    </div>
                    <div class="mt-4">
                        <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20prendre%20conseil%20pour%20un%20traitement." target="_blank" class="btn-gold mr-3">
                            Poser vos questions sur WhatsApp
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Treatments Section -->
    <section id="traitements" class="py-5" style="background: #f8fafc;">
        <div class="container py-4">
            <div class="text-center max-w-700 mx-auto mb-5">
                <span class="text-uppercase text-gold font-weight-bold" style="font-size: 13px; letter-spacing: 2px;">Protocoles Signatures</span>
                <h2 class="display-5 font-serif font-weight-bold mt-2" style="color: var(--primary-emerald);">Nos Traitements Personnalisés</h2>
                <p class="text-muted" style="max-width: 650px; margin: 0 auto;">
                    Chaque intervention est minutieusement adaptée selon votre morphologie, vos attentes et l'âge de votre peau.
                </p>
            </div>

            <div class="row">
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-eye fa-2x"></i></span>
                                <span class="badge badge-light border text-gold px-2 py-1">Best-Seller</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">Vallée des Larmes & Cernes</h4>
                            <p class="text-muted small" style="line-height: 1.6;">
                                Comblement subtil des creux sous les yeux à l'acide hyaluronique fluide. Illumine instantanément le regard, efface l'air fatigué et redonne fraîcheur sans gonflement.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>Demander ce traitement</span> <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-gem fa-2x"></i></span>
                                <span class="badge badge-light border text-emerald px-2 py-1">Volume & Lift</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">Pommettes & Effet Lift</h4>
                            <p class="text-muted small" style="line-height: 1.6;">
                                Restauration délicate des volumes perdus suite à un régime, au sport ou au temps. Remonte les traits affaissés et rétablit l'équilibre en "triangle de jeunesse".
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>Demander ce traitement</span> <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-user-check fa-2x"></i></span>
                                <span class="badge badge-light border text-gold px-2 py-1">Harmonie</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">Jawline & Profil Texas</h4>
                            <p class="text-muted small" style="line-height: 1.6;">
                                Redéfinition nette de l'angle mandibulaire et projection discrète du menton. Affine l'ovale du visage pour un profil structuré et élégant sous tous les angles.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>Demander ce traitement</span> <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-kiss-wink-heart fa-2x"></i></span>
                                <span class="badge badge-light border text-emerald px-2 py-1">Subtil</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">Lèvres Naturelles & Hydratation</h4>
                            <p class="text-muted small" style="line-height: 1.6;">
                                Définition de l'arc de Cupidon et hydratation profonde des lèvres sans excès ni projection artificielle. Révèle la douceur et la sensualité naturelle de votre sourire.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>Demander ce traitement</span> <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-smile fa-2x"></i></span>
                                <span class="badge badge-light border text-gold px-2 py-1">Anti-Âge</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">Botox & Lissage Frontal</h4>
                            <p class="text-muted small" style="line-height: 1.6;">
                                Lissage tout en nuance des rides du lion, du front et de la patte d'oie. Votre regard reste vivant, expressif et détendu, sans aucun effet figé ni sourcil tiré.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>Demander ce traitement</span> <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-spa fa-2x"></i></span>
                                <span class="badge badge-light border text-emerald px-2 py-1">Glow & Teint</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">Skinbooster Éclat & Fermeté</h4>
                            <p class="text-muted small" style="line-height: 1.6;">
                                Micro-injections d'acide hyaluronique non réticulé enrichi en vitamines. Réhydrate le derme en profondeur pour un effet "glow" durable, sans filtre ni fond de teint.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>Demander ce traitement</span> <i class="fas fa-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Case Study Section (Zineb) -->
    <section id="cas-pratique" class="py-5" style="background: #ffffff;">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-5 mb-4 mb-lg-0 text-center">
                    <div class="position-relative d-inline-block">
                        <img src="assets/img/consultation-zineb.jpg" alt="Cas Réel Zineb Dr Hanane Kashi" class="img-fluid rounded-lg shadow-lg" style="max-height: 480px; object-fit: cover; border: 4px solid var(--primary-gold);">
                        <div class="position-absolute bg-white px-3 py-2 rounded-pill shadow text-dark font-weight-bold" style="top: 15px; left: 15px; font-size: 12px;">
                            <span class="text-danger mr-1">●</span> Cas Patient Authentique
                        </div>
                    </div>
                </div>
                <div class="col-lg-7 pl-lg-5">
                    <span class="badge badge-warning text-dark px-3 py-1 font-weight-bold mb-2">Résultat Avant / Après</span>
                    <h2 class="display-5 font-serif font-weight-bold mb-3" style="color: var(--primary-emerald);">
                        "Sublimer sans figer" : L'histoire de Zineb
                    </h2>
                    
                    <div class="mb-3">
                        <h6 class="font-weight-bold text-dark mb-1">
                            <i class="fas fa-stethoscope text-gold mr-2"></i> Le Défi Initial :
                        </h6>
                        <p class="text-muted small" style="line-height: 1.6;">
                            Après une période intensive de sport et un régime, Zineb a perdu le volume naturel de ses joues et de ses pommettes, créant un creux marqué au niveau des cernes (vallée des larmes) qui lui donnait un air constamment fatigué.
                        </p>
                    </div>

                    <div class="mb-3">
                        <h6 class="font-weight-bold text-dark mb-1">
                            <i class="fas fa-magic text-emerald mr-2"></i> Le Protocole Sur-Mesure du Dr. Kashi :
                        </h6>
                        <p class="text-muted small" style="line-height: 1.6;">
                            • Comblement doux de la vallée des larmes pour défatiguer le regard.<br>
                            • Restauration légère du volume des pommettes pour recréer l'arrondi naturel.<br>
                            • Définition subtile de la jawline et du menton.<br>
                            • Touche d'hydratation discrète sur les lèvres : <em>"Ça sera naturel, on garde vos formes tout en harmonisant."</em>
                        </p>
                    </div>

                    <div class="testimonial-quote-box">
                        <p class="mb-2" style="font-size: 16px; font-weight: 600; color: #1e293b; direction: rtl; text-align: right; font-family: 'Cairo', sans-serif;">
                            "الريزولتا كانت زوينة بزاف، لدرجة عطاتني ديك الثقة أنني نتصور غير بكاميرا عادية، بلا سناپ، بلا فيلتر، بلا والو. وصحاباتي كيقولوا ليا فيكم شي تغيير مي زوين و ناتوريل!"
                        </p>
                        <p class="mb-0 text-muted small" style="font-style: italic;">
                            — Zineb, patiente du Dr. Hanane Kashi à Casablanca
                        </p>
                    </div>

                    <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20j'ai%20vu%20le%20r%C3%A9sultat%20de%20Zineb%20et%20je%20souhaite%20un%20diagnostic%20similaire." target="_blank" class="btn-whatsapp">
                        <i class="fab fa-whatsapp"></i> Je veux un diagnostic similaire
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Appointment Section -->
    <section id="rendez-vous" class="py-5 bg-emerald text-light">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <span class="badge px-3 py-1 mb-2 text-gold border border-warning" style="background: rgba(0,0,0,0.2);">Consultation Privée</span>
                    <h2 class="display-5 font-serif font-weight-bold text-white mb-3">
                        Prenez Rendez-vous au Cabinet à Casablanca
                    </h2>
                    <p style="color: #cbd5e1; line-height: 1.7;">
                        La première étape vers votre harmonie faciale commence par une consultation d'évaluation approfondie avec le Dr. Hanane Kashi. 
                    </p>
                    <ul class="list-unstyled mt-4" style="color: #e2e8f0;">
                        <li class="mb-3 d-flex align-items-center">
                            <i class="fas fa-check-circle text-gold mr-3 fa-lg"></i>
                            <span>Analyse morphologique et proposition d'un protocole adapté</span>
                        </li>
                        <li class="mb-3 d-flex align-items-center">
                            <i class="fas fa-check-circle text-gold mr-3 fa-lg"></i>
                            <span>Devis transparent et explications détaillées avant chaque acte</span>
                        </li>
                        <li class="mb-3 d-flex align-items-center">
                            <i class="fas fa-check-circle text-gold mr-3 fa-lg"></i>
                            <span>Discrétion totale et respect absolu du secret médical</span>
                        </li>
                    </ul>
                    <div class="mt-4 pt-2">
                        <p class="mb-1 text-gold font-weight-bold">Besoin d'une réponse rapide ?</p>
                        <h4 class="text-white font-weight-bold">
                            <i class="fas fa-phone-alt mr-2 text-gold"></i> 05 20 60 44 84
                        </h4>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="bg-white text-dark rounded-lg p-4 p-md-5 shadow-lg">
                        <h3 class="font-serif font-weight-bold mb-2 text-emerald">Réserver une Consultation</h3>
                        <p class="text-muted small mb-4">Remplissez le formulaire, nous vous contacterons sur WhatsApp pour confirmer votre créneau.</p>
                        
                        <form onsubmit="handleAppointmentSubmit(event)">
                            <div class="form-group mb-3">
                                <label class="small font-weight-bold text-muted">Nom & Prénom</label>
                                <input type="text" id="patientName" class="form-control" placeholder="Ex: Sara Benjelloun" required style="height: 48px; border-radius: 8px;">
                            </div>
                            <div class="form-group mb-3">
                                <label class="small font-weight-bold text-muted">Numéro de Téléphone (WhatsApp)</label>
                                <input type="tel" id="patientPhone" class="form-control" placeholder="06XXXXXXXX" required style="height: 48px; border-radius: 8px;">
                            </div>
                            <div class="form-group mb-3">
                                <label class="small font-weight-bold text-muted">Traitement Souhaité</label>
                                <select id="treatmentType" class="form-control" style="height: 48px; border-radius: 8px;">
                                    <option value="Vallée des Larmes & Cernes">Vallée des Larmes & Cernes</option>
                                    <option value="Pommettes & Restauration Volume">Pommettes & Restauration Volume</option>
                                    <option value="Jawline & Profil Texas">Jawline & Profil Texas</option>
                                    <option value="Lèvres Naturelles">Lèvres Naturelles</option>
                                    <option value="Botox & Rides d'Expression">Botox & Rides d'Expression</option>
                                    <option value="Skinbooster & Éclat">Skinbooster & Éclat</option>
                                    <option value="Consultation & Diagnostic Global">Autre / Diagnostic Global</option>
                                </select>
                            </div>
                            <div class="form-group mb-4">
                                <label class="small font-weight-bold text-muted">Jour préféré</label>
                                <input type="date" id="preferredDate" class="form-control" style="height: 48px; border-radius: 8px;">
                            </div>
                            <button type="submit" class="btn btn-block btn-gold font-weight-bold" style="height: 52px; font-size: 15px; border-radius: 8px;">
                                <i class="fab fa-whatsapp mr-2"></i> Envoyer et Confirmer sur WhatsApp
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section id="temoignages" class="py-5" style="background: #f8fafc;">
        <div class="container py-4">
            <div class="text-center max-w-700 mx-auto mb-5">
                <span class="text-uppercase text-gold font-weight-bold" style="font-size: 13px; letter-spacing: 2px;">Retours d'Expérience</span>
                <h2 class="display-5 font-serif font-weight-bold mt-2" style="color: var(--primary-emerald);">Ce que disent nos patientes</h2>
                <p class="text-muted">Des témoignages spontanés qui reflètent notre engagement pour le naturel et la bienveillance.</p>
            </div>

            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="treatment-card p-4">
                        <div class="text-warning mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-muted small" style="line-height: 1.6;">
                            "J'avais une peur bleue d'avoir un visage gonflé ou figé. Dr. Kashi m'a mise en confiance totale. Mes cernes ont disparu et mon entourage me dit juste que j'ai l'air reposée comme après des vacances !"
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div class="rounded-circle bg-emerald text-white d-flex align-items-center justify-content-center font-weight-bold mr-3" style="width: 42px; height: 42px;">
                                MK
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-dark">Meryem K.</h6>
                                <small class="text-muted">Casablanca • Vallée des larmes</small>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 mb-4">
                    <div class="treatment-card p-4">
                        <div class="text-warning mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-muted small" style="line-height: 1.6;">
                            "Le travail de Dr. Hanane est d'une finesse incroyable. Elle a su redessiner ma mâchoire sans alourdir le bas de mon visage. La micro-canule ne fait absolument pas mal. Médecin très professionnelle."
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div class="rounded-circle bg-gold text-white d-flex align-items-center justify-content-center font-weight-bold mr-3" style="width: 42px; height: 42px;">
                                LE
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-dark">Leila E.</h6>
                                <small class="text-muted">Casablanca • Profil Texas</small>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 mb-4">
                    <div class="treatment-card p-4">
                        <div class="text-warning mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-muted small" style="line-height: 1.6;">
                            "Tellement heureuse du résultat ! Plus besoin de retoucher mes photos ni de mettre de filtres. Tout est naturel et doux. Merci mille fois Dr. Kashi pour votre écoute et votre talent."
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div class="rounded-circle bg-emerald text-white d-flex align-items-center justify-content-center font-weight-bold mr-3" style="width: 42px; height: 42px;">
                                ZB
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-dark">Zineb B.</h6>
                                <small class="text-muted">Casablanca • Harmonisation globale</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-5" style="background: #ffffff;">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <span class="text-uppercase text-gold font-weight-bold" style="font-size: 13px; letter-spacing: 2px;">Nous Trouver</span>
                    <h2 class="display-5 font-serif font-weight-bold mt-2 mb-3" style="color: var(--primary-emerald);">Cabinet Médical Casablanca</h2>
                    <p class="text-muted mb-4" style="line-height: 1.7;">
                        Un cadre accueillant, confidentiel et équipé des technologies les plus récentes en médecine esthétique.
                    </p>
                    <div class="d-flex mb-3">
                        <i class="fas fa-map-marked-alt text-gold mr-3 fa-lg mt-1"></i>
                        <div>
                            <h6 class="font-weight-bold mb-0 text-dark">Adresse du Cabinet</h6>
                            <p class="text-muted small">Casablanca, Maroc (Sur rendez-vous préalable)</p>
                        </div>
                    </div>
                    <div class="d-flex mb-3">
                        <i class="fas fa-phone-alt text-emerald mr-3 fa-lg mt-1"></i>
                        <div>
                            <h6 class="font-weight-bold mb-0 text-dark">Téléphone Fixe</h6>
                            <p class="text-muted small"><a href="tel:0520604484" class="text-dark font-weight-bold">05 20 60 44 84</a></p>
                        </div>
                    </div>
                    <div class="d-flex mb-3">
                        <i class="fab fa-whatsapp text-success mr-3 fa-lg mt-1"></i>
                        <div>
                            <h6 class="font-weight-bold mb-0 text-dark">WhatsApp & Mobile</h6>
                            <p class="text-muted small"><a href="https://wa.me/212600980685" target="_blank" class="text-dark font-weight-bold">06 00 98 06 85</a></p>
                        </div>
                    </div>
                    <div class="d-flex">
                        <i class="fab fa-facebook-f text-primary mr-3 fa-lg mt-1"></i>
                        <div>
                            <h6 class="font-weight-bold mb-0 text-dark">Page Facebook Officielle</h6>
                            <p class="text-muted small"><a href="https://web.facebook.com/people/Docteur-hanane-kashi/100091182893832/" target="_blank" class="text-primary font-weight-bold">Docteur hanane kashi</a></p>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="p-4 rounded-lg bg-light border text-center shadow-sm">
                        <div class="mb-3">
                            <i class="far fa-clock text-gold fa-3x"></i>
                        </div>
                        <h4 class="font-serif font-weight-bold text-dark mb-2">Horaires d'Ouverture</h4>
                        <p class="text-muted small mb-4">Consultations personnalisées sur rendez-vous pour assurer une prise en charge exclusive sans attente.</p>
                        <div class="d-flex justify-content-between py-2 border-bottom">
                            <span class="font-weight-bold text-dark">Lundi – Vendredi</span>
                            <span class="text-muted">09:30 – 18:30</span>
                        </div>
                        <div class="d-flex justify-content-between py-2 border-bottom">
                            <span class="font-weight-bold text-dark">Samedi</span>
                            <span class="text-muted">09:30 – 14:00</span>
                        </div>
                        <div class="d-flex justify-content-between py-2">
                            <span class="font-weight-bold text-dark">Dimanche</span>
                            <span class="text-danger font-weight-bold">Fermé</span>
                        </div>
                        <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20conna%C3%AEtre%20vos%20disponibilit%C3%A9s." target="_blank" class="btn-whatsapp btn-block mt-4 justify-content-center">
                            <i class="fab fa-whatsapp"></i> Vérifier les disponibilités
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-light py-4" style="background-color: #0b1e18 !important; border-top: 1px solid rgba(255,255,255,0.08);">
        <div class="container text-center text-md-left">
            <div class="row align-items-center">
                <div class="col-md-6 mb-3 mb-md-0 d-flex align-items-center justify-content-center justify-content-md-start">
                    <img src="assets/img/dr-kashi-logo.jpg" alt="Logo Dr Hanane Kashi" style="height: 44px; width: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #c5a059;" class="mr-3">
                    <div>
                        <h5 class="font-serif text-white mb-0">Docteur Hanane Kashi</h5>
                        <p class="small text-muted mb-0">Médecine Esthétique, Injections & Anti-Âge à Casablanca.</p>
                    </div>
                </div>
                <div class="col-md-6 text-center text-md-right">
                    <p class="small text-muted mb-0">
                        &copy; 2026 Cabinet Dr. Hanane Kashi. Tous droits réservés. <br>
                        Développé pour une expérience patient optimale.
                    </p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp -->
    <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20prendre%20un%20rendez-vous%20de%20consultation." target="_blank" class="floating-whatsapp" aria-label="WhatsApp Dr Hanane Kashi">
        <i class="fab fa-whatsapp"></i>
    </a>

    <!-- Sticky Mobile Contact Bar -->
    <div class="sticky-mobile-bar">
        <a href="tel:0520604484" class="sticky-call">
            <i class="fas fa-phone-alt"></i> 05 20 60 44 84
        </a>
        <a href="https://wa.me/212600980685?text=Bonjour%20Dr.%20Hanane%20Kashi,%20je%20souhaite%20r%C3%A9server%20une%20consultation." target="_blank" class="sticky-wa">
            <i class="fab fa-whatsapp"></i> WhatsApp
        </a>
    </div>

    <!-- Scripts -->
    <script src="assets/js/jquery-1.12.4.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/bootsnav.js"></script>
    <script>
        function handleAppointmentSubmit(e) {
            e.preventDefault();
            var name = document.getElementById('patientName').value.trim();
            var phone = document.getElementById('patientPhone').value.trim();
            var treatment = document.getElementById('treatmentType').value;
            var date = document.getElementById('preferredDate').value;

            var msg = "Bonjour Dr. Hanane Kashi,%0A%0AJe souhaite réserver une consultation :%0A" +
                      "• Nom : " + encodeURIComponent(name) + "%0A" +
                      "• Téléphone : " + encodeURIComponent(phone) + "%0A" +
                      "• Traitement : " + encodeURIComponent(treatment);
            if (date) {
                msg += "%0A• Date souhaitée : " + encodeURIComponent(date);
            }
            msg += "%0A%0AMerci de me confirmer le créneau.";

            window.open("https://wa.me/212600980685?text=" + msg, "_blank");
        }
    </script>
</body>
</html>
"""
    return head + body

def generate_arabic_page():
    head = get_head(
        title="الدكتورة حنان كاشي | طب التجميل ومكافحة الشيخوخة بالدار البيضاء",
        desc="إبراز الجمال الطبيعي دون تجميد الملامح. حقن حمض الهيالورونيك، البوتوكس، فيلر وادي الدموع، تحديد الفك تكساس بالدار البيضاء.",
        is_rtl=True
    )

    body = """<body>
    <!-- Top Bar -->
    <div class="top-bar-area bg-emerald text-light py-2" style="border-bottom: 1px solid rgba(255,255,255,0.1);">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 col-12 text-center text-lg-right mb-2 mb-lg-0">
                    <span style="font-size: 14px;">
                        <i class="fas fa-map-marker-alt text-gold ml-1"></i> عيادة طب التجميل — الدار البيضاء، المغرب
                    </span>
                </div>
                <div class="col-lg-6 col-12 text-center text-lg-left d-flex justify-content-center justify-content-lg-start align-items-center">
                    <a href="tel:0520604484" class="text-light ml-3 font-weight-bold" style="font-size: 14px;">
                        <i class="fas fa-phone-alt text-gold ml-1"></i> 05 20 60 44 84
                    </a>
                    <a href="https://wa.me/212600980685?text=السلام%20عليكم%20دكتورة%20حنان%20كاشي،%20أود%20حجز%20موعد%20استشارة." target="_blank" class="text-light font-weight-bold ml-3" style="font-size: 14px;">
                        <i class="fab fa-whatsapp text-success ml-1"></i> 06 00 98 06 85
                    </a>
                    <!-- Language Switcher -->
                    <a href="index.html" class="lang-switch-btn mr-2">
                        🇫🇷 Français
                    </a>
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
                    <a class="navbar-brand d-flex align-items-center" href="ar.html" style="padding: 6px 0;">
                        <img src="assets/img/dr-kashi-logo.jpg" alt="شعار الدكتورة حنان كاشي" style="height: 52px; width: 52px; border-radius: 50%; object-fit: cover; border: 2px solid #c5a059;" class="ml-2">
                        <div style="line-height: 1.2;">
                            <span class="font-serif font-weight-bold" style="font-size: 22px; color: var(--primary-emerald); letter-spacing: -0.5px;">الدكتورة حنان كاشي</span>
                            <span class="d-block text-muted" style="font-size: 11px; letter-spacing: 1px;">طب التجميل ومكافحة الشيخوخة</span>
                        </div>
                    </a>
                </div>

                <div class="collapse navbar-collapse" id="navbar-menu">
                    <ul class="nav navbar-nav navbar-left" data-in="fadeInDown" data-out="fadeOutUp">
                        <li><a href="#home">الرئيسية</a></li>
                        <li><a href="#docteur">عن الدكتورة</a></li>
                        <li><a href="#traitements">العلاجات</a></li>
                        <li><a href="#cas-pratique">قبل / بعد</a></li>
                        <li><a href="#temoignages">آراء المريضات</a></li>
                        <li><a href="#contact">تواصل معنا</a></li>
                        <li class="d-none d-lg-block mr-3">
                            <a href="#rendez-vous" class="btn-gold" style="padding: 8px 22px !important; margin-top: 18px; color: #fff !important; font-size: 14px;">حجز موعد</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <div class="hero-aesthetic">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-7">
                    <span class="badge px-3 py-2 text-uppercase mb-3" style="background: rgba(197, 160, 89, 0.25); color: #fce7b2; border: 1px solid #c5a059; font-size: 13px; letter-spacing: 1px; border-radius: 30px;">
                        ✨ طب التجميل الدقيق بالدار البيضاء
                    </span>
                    <h1 class="display-4 font-weight-bold mb-3" style="line-height: 1.3; text-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                        إبراز الجمال دون تجميد، <br>
                        <span class="text-gold" style="font-style: italic;">وتناسق الملامح دون تغيير الهوية.</span>
                    </h1>
                    <p class="lead mb-4" style="color: #e2e8f0; font-size: 19px; max-width: 600px;">
                        لكل وجه تناسقه الخاص وسحره الفريد. تقدم الدكتورة حنان كاشي بروتوكولات حقن مخصصة ودقيقة لاستعادة امتلاء الوجه، إخفاء علامات التعب، وإبراز ملامحك بكل سرية وطبيعية.
                    </p>
                    <div class="d-flex flex-wrap gap-3">
                        <a href="https://wa.me/212600980685?text=السلام%20عليكم%20دكتورة%20حنان%20كاشي،%20أود%20حجز%20موعد%20استشارة%20بالعيادة." target="_blank" class="btn-whatsapp ml-3 mb-2">
                            <i class="fab fa-whatsapp" style="font-size: 20px;"></i> حجز استشارة عبر واتساب
                        </a>
                        <a href="#traitements" class="btn btn-outline-light mb-2 font-weight-bold" style="border-radius: 50px; padding: 13px 26px;">
                            اكتشاف العلاجات
                        </a>
                    </div>
                </div>
                <div class="col-lg-5 mt-5 mt-lg-0 text-center">
                    <div class="doctor-badge-card text-dark position-relative mx-auto" style="max-width: 380px;">
                        <div class="overflow-hidden rounded-circle mx-auto mb-3" style="width: 220px; height: 220px; border: 5px solid #c5a059; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
                            <img src="assets/img/dr-hanane-kashi.jpg" alt="الدكتورة حنان كاشي" class="img-fluid w-100 h-100" style="object-fit: cover;">
                        </div>
                        <h4 class="font-serif font-weight-bold mb-1" style="color: var(--primary-emerald);">الدكتورة حنان كاشي</h4>
                        <p class="text-muted mb-2 font-weight-bold" style="font-size: 14px;">أخصائية طب التجميل ومكافحة الشيخوخة</p>
                        <p class="small text-muted mb-3" style="line-height: 1.5;">الدار البيضاء • نتائج طبيعية • منتجات معتمدة عالمياً CE & FDA</p>
                        <div class="border-top pt-3 d-flex justify-content-around text-center">
                            <div>
                                <strong class="d-block text-emerald font-weight-bold" style="font-size: 18px;">100%</strong>
                                <span class="text-muted small">مخصص لك</span>
                            </div>
                            <div>
                                <strong class="d-block text-emerald font-weight-bold" style="font-size: 18px;">طبيعي</strong>
                                <span class="text-muted small">دون تجميد</span>
                            </div>
                            <div>
                                <strong class="d-block text-emerald font-weight-bold" style="font-size: 18px;">مريح</strong>
                                <span class="text-muted small">بدون ألم</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Trust Strip -->
    <div class="py-4" style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="row text-center">
                <div class="col-md-4 col-12 mb-3 mb-md-0">
                    <div class="d-flex align-items-center justify-content-center">
                        <i class="fas fa-certificate text-gold ml-3" style="font-size: 28px;"></i>
                        <div class="text-right">
                            <h6 class="mb-0 font-weight-bold text-dark">منتجات مرخصة CE & FDA</h6>
                            <small class="text-muted">أجود أنواع حمض الهيالورونيك والبوتوكس</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 col-12 mb-3 mb-md-0">
                    <div class="d-flex align-items-center justify-content-center">
                        <i class="fas fa-feather-alt text-emerald ml-3" style="font-size: 28px;"></i>
                        <div class="text-right">
                            <h6 class="mb-0 font-weight-bold text-dark">نتيجة سرية وطبيعية 100%</h6>
                            <small class="text-muted">"إبراز الجمال دون أي مبالغة أو تصنّع"</small>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="d-flex align-items-center justify-content-center">
                        <i class="fas fa-heart text-danger ml-3" style="font-size: 28px;"></i>
                        <div class="text-right">
                            <h6 class="mb-0 font-weight-bold text-dark">راحة المريضة والإنصات</h6>
                            <small class="text-muted">تشخيص وجهي دقيق قبل أي إجراء</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- About Section -->
    <section id="docteur" class="py-5" style="background: #ffffff;">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0 text-center">
                    <div class="position-relative d-inline-block">
                        <img src="assets/img/dr-kashi-cabinet-wall.jpg" alt="عيادة الدكتورة حنان كاشي مع الشعار الجداري الذهبي" class="img-fluid rounded-lg shadow-lg" style="max-height: 460px; object-fit: cover; border: 4px solid #fff;">
                        <div class="position-absolute p-3 rounded-lg bg-emerald text-light text-right shadow" style="bottom: -20px; left: -15px; max-width: 260px;">
                            <span class="d-block text-gold font-weight-bold" style="font-size: 14px;">منهجية الدكتورة كاشي</span>
                            <small style="font-size: 13px; line-height: 1.4;">بروتوكول احترافي يحترم البنية العظمية والامتلاء الطبيعي لوجهك.</small>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 pr-lg-5">
                    <span class="text-uppercase text-gold font-weight-bold" style="font-size: 14px; letter-spacing: 1px;">الفلسفة والخبرة الطبية</span>
                    <h2 class="display-5 font-serif font-weight-bold mt-2 mb-3" style="color: var(--primary-emerald);">
                        فن الكشف عن جمالك دون تغييره
                    </h2>
                    <p class="text-muted" style="line-height: 1.8;">
                        في عالم طب التجميل، السر الحقيقي للإجراء الناجح هو ألا يلاحظ أحد أنك قمت بأي حقن، بل يلاحظ الجميع إشراقة وجهك ونضارتك الطبيعية!
                    </p>
                    <p class="text-muted" style="line-height: 1.8;">
                        في عيادة الدكتورة حنان كاشي بالدار البيضاء، نعتمد على تقنية <strong>الميكرو-كانيل المرنة (Micro-canule)</strong>، التي تضمن إجراءً مريحاً وبدون كدمات، مع العودة الفورية لحياتك اليومية بكل ثقة.
                    </p>
                    <div class="row mt-4">
                        <div class="col-sm-6 mb-3">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-emerald ml-2" style="font-size: 20px;"></i>
                                <span class="font-weight-bold text-dark">تشخيص كامل وتفصيلي للوجه</span>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-emerald ml-2" style="font-size: 20px;"></i>
                                <span class="font-weight-bold text-dark">صفر مظهر مصطنع أو منفوخ</span>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-emerald ml-2" style="font-size: 20px;"></i>
                                <span class="font-weight-bold text-dark">حقن دقيقة ومخصصة</span>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-3">
                            <div class="d-flex align-items-center">
                                <i class="fas fa-check-circle text-emerald ml-2" style="font-size: 20px;"></i>
                                <span class="font-weight-bold text-dark">متابعة طبية دقيقة ومستمرة</span>
                            </div>
                        </div>
                    </div>
                    <div class="mt-4">
                        <a href="https://wa.me/212600980685?text=السلام%20عليكم%20دكتورة%20حنان،%20أود%20استشارة%20حول%20علاج%20مناسب%20لوجهي." target="_blank" class="btn-gold ml-3">
                            تحدثي مع الدكتورة عبر واتساب
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Treatments Section -->
    <section id="traitements" class="py-5" style="background: #f8fafc;">
        <div class="container py-4">
            <div class="text-center max-w-700 mx-auto mb-5">
                <span class="text-uppercase text-gold font-weight-bold" style="font-size: 14px; letter-spacing: 1px;">العلاجات المتميزة</span>
                <h2 class="display-5 font-serif font-weight-bold mt-2" style="color: var(--primary-emerald);">علاجات مخصصة لجمالك</h2>
                <p class="text-muted" style="max-width: 650px; margin: 0 auto;">
                    كل خطوة علاجية مدروسة بعناية فائقة لتلائم ملامح وجهك، أهدافك، ونضارة بشرتك.
                </p>
            </div>

            <div class="row">
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-eye fa-2x"></i></span>
                                <span class="badge badge-light border text-gold px-2 py-1">الأكثر طلباً</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">وادي الدموع وعلاج الهالات</h4>
                            <p class="text-muted small" style="line-height: 1.7;">
                                ملء دقيق لتجويف تحت العين بحمض الهيالورونيك فائق النقاء. يزيل علامات التعب والإرهاق ويعيد النضارة والإشراق لعينيك فوراً.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>طلب هذا العلاج</span> <i class="fas fa-arrow-left"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-gem fa-2x"></i></span>
                                <span class="badge badge-light border text-emerald px-2 py-1">امتلاء وشد</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">الخدود ورفع الوجنتين (Pommettes)</h4>
                            <p class="text-muted small" style="line-height: 1.7;">
                                استعادة امتلاء الخدود بعد فقدان الوزن أو الريجيم والرياضة. يعيد رفع ملامح الوجه المترهلة ويعيد رسم مثلث الشباب الطبيعي.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>طلب هذا العلاج</span> <i class="fas fa-arrow-left"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-user-check fa-2x"></i></span>
                                <span class="badge badge-light border text-gold px-2 py-1">تناسق الفك</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">تحديد الفك والذقن (Jawline Texas)</h4>
                            <p class="text-muted small" style="line-height: 1.7;">
                                تحديد زوايا الفك بدقة وإبراز خفيف للذقن. يمنح الوجه إطاراً مشدوداً ومرسوماً من كل الزوايا بدون أي خشونة في الملامح.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>طلب هذا العلاج</span> <i class="fas fa-arrow-left"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-kiss-wink-heart fa-2x"></i></span>
                                <span class="badge badge-light border text-emerald px-2 py-1">ناعم وطبيعي</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">فيلر الشفاه الطبيعي والترطيب</h4>
                            <p class="text-muted small" style="line-height: 1.7;">
                                تحديد قوس الشفاه وترطيبها بعمق دون بروز مبالغ فيه. يبرز نعومة وجمال ابتسامتك الطبيعية دون أي نفخ مصطنع.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>طلب هذا العلاج</span> <i class="fas fa-arrow-left"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-smile fa-2x"></i></span>
                                <span class="badge badge-light border text-gold px-2 py-1">مكافحة التجاعيد</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">بوتوكس الجبهة ومحيط العين</h4>
                            <p class="text-muted small" style="line-height: 1.7;">
                                تنعيم تجاعيد الجبهة، بين الحاجبين، ومحيط العين مع الحفاظ الكامل على حركة تعابير وجهك الحية دون أي تجميد.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>طلب هذا العلاج</span> <i class="fas fa-arrow-left"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="treatment-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="p-2 rounded-circle bg-light text-emerald"><i class="fas fa-spa fa-2x"></i></span>
                                <span class="badge badge-light border text-emerald px-2 py-1">نضارة البشرة</span>
                            </div>
                            <h4 class="font-serif font-weight-bold text-dark mb-2">سكين بوستر والميزوثيرابي</h4>
                            <p class="text-muted small" style="line-height: 1.7;">
                                حقن مغذية من حمض الهيالورونيك والفيتامينات في أعماق البشرة. تعيد لمعان البشرة ونضارتها الزجاجية بدون فلاتر.
                            </p>
                        </div>
                        <div class="border-top pt-3 mt-3">
                            <a href="#rendez-vous" class="font-weight-bold text-emerald d-flex justify-content-between align-items-center">
                                <span>طلب هذا العلاج</span> <i class="fas fa-arrow-left"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Case Study Section (Zineb) -->
    <section id="cas-pratique" class="py-5" style="background: #ffffff;">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-5 mb-4 mb-lg-0 text-center">
                    <div class="position-relative d-inline-block">
                        <img src="assets/img/consultation-zineb.jpg" alt="حالة حقيقية زينب الدكتورة حنان كاشي" class="img-fluid rounded-lg shadow-lg" style="max-height: 480px; object-fit: cover; border: 4px solid var(--primary-gold);">
                        <div class="position-absolute bg-white px-3 py-2 rounded-pill shadow text-dark font-weight-bold" style="top: 15px; right: 15px; font-size: 13px;">
                            <span class="text-danger ml-1">●</span> حالة واقعية حقيقية
                        </div>
                    </div>
                </div>
                <div class="col-lg-7 pr-lg-5">
                    <span class="badge badge-warning text-dark px-3 py-1 font-weight-bold mb-2">نتيجة قبل / بعد</span>
                    <h2 class="display-5 font-serif font-weight-bold mb-3" style="color: var(--primary-emerald);">
                        "تجميل دون تصنع" : قصة المريضة زينب
                    </h2>
                    
                    <div class="mb-3">
                        <h6 class="font-weight-bold text-dark mb-1">
                            <i class="fas fa-stethoscope text-gold ml-2"></i> المشكلة الأولية :
                        </h6>
                        <p class="text-muted small" style="line-height: 1.7;">
                            بعد فترة مكثفة من الرياضة ونظام حمية غذائي (ريجيم)، فقد وجه زينب امتلائه الطبيعي، مما تسبب في ظهور تجويف تحت العينين (وادي الدموع) وأعطاها مظهراً يبدو متعباً باستمرار.
                        </p>
                    </div>

                    <div class="mb-3">
                        <h6 class="font-weight-bold text-dark mb-1">
                            <i class="fas fa-magic text-emerald ml-2"></i> خطة العلاج من الدكتورة حنان كاشي :
                        </h6>
                        <p class="text-muted small" style="line-height: 1.7;">
                            • ملء وادي الدموع لإزالة التعب من النظرة.<br>
                            • إعادة الامتلاء الطبيعي للوجنتين والخدود لاستعادة الاستدارة الحيوية.<br>
                            • لمسة خفيفة لتحديد الفك والذقن (تكساس).<br>
                            • ترطيب ولمسة خفيفة للشفتين : <em>"داكشي غادي يكون ناتوريل، غانخليو ليك لي فورم ديالك مع تناسق زوين."</em>
                        </p>
                    </div>

                    <div class="testimonial-quote-box">
                        <p class="mb-2" style="font-size: 17px; font-weight: 700; color: #1e293b; line-height: 1.6;">
                            "الريزولتا كانت زوينة بزاف، لدرجة عطاتني ديك الثقة أنني نتصور غير بكاميرا عادية، بلا سناپ، بلا فيلتر، بلا والو. وصحاباتي كيقولوا ليا فيكم شي تغيير مي زوين و ناتوريل!"
                        </p>
                        <p class="mb-0 text-muted small" style="font-style: italic;">
                            — زينب، مريضة عند الدكتورة حنان كاشي بالدار البيضاء
                        </p>
                    </div>

                    <a href="https://wa.me/212600980685?text=السلام%20عليكم%20دكتورة%20حنان%20كاشي،%20شفت%20حالة%20زينب%20وبغيت%20استشارة%20مماثلة." target="_blank" class="btn-whatsapp">
                        <i class="fab fa-whatsapp"></i> أريد تشخيصاً مماثلاً لحالتي
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Appointment Section -->
    <section id="rendez-vous" class="py-5 bg-emerald text-light">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <span class="badge px-3 py-1 mb-2 text-gold border border-warning" style="background: rgba(0,0,0,0.2);">استشارة خاصة</span>
                    <h2 class="display-5 font-serif font-weight-bold text-white mb-3">
                        احجزي موعدك بالعيادة في الدار البيضاء
                    </h2>
                    <p style="color: #cbd5e1; line-height: 1.8;">
                        أول خطوة نحو تناسق وجهك وإشراقته تبدأ باستشارة تقييم شاملة ودقيقة مع الدكتورة حنان كاشي.
                    </p>
                    <ul class="list-unstyled mt-4" style="color: #e2e8f0;">
                        <li class="mb-3 d-flex align-items-center">
                            <i class="fas fa-check-circle text-gold ml-3 fa-lg"></i>
                            <span>تشخيص كامل للملامح وخطة علاجية مخصصة لك تماماً</span>
                        </li>
                        <li class="mb-3 d-flex align-items-center">
                            <i class="fas fa-check-circle text-gold ml-3 fa-lg"></i>
                            <span>شفافية تامة في التكلفة وشرح تفصيلي قبل أي إجراء</span>
                        </li>
                        <li class="mb-3 d-flex align-items-center">
                            <i class="fas fa-check-circle text-gold ml-3 fa-lg"></i>
                            <span>سرية مطلقة واحترام كامل للخصوصية الطبية</span>
                        </li>
                    </ul>
                    <div class="mt-4 pt-2">
                        <p class="mb-1 text-gold font-weight-bold">هل تفضلين الاتصال السريع؟</p>
                        <h4 class="text-white font-weight-bold">
                            <i class="fas fa-phone-alt ml-2 text-gold"></i> 05 20 60 44 84
                        </h4>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="bg-white text-dark rounded-lg p-4 p-md-5 shadow-lg">
                        <h3 class="font-serif font-weight-bold mb-2 text-emerald">حجز موعد استشارة</h3>
                        <p class="text-muted small mb-4">املئي بياناتك، وسنتواصل معك عبر واتساب لتأكيد وقت الموعد المناسب لك.</p>
                        
                        <form onsubmit="handleAppointmentSubmit(event)">
                            <div class="form-group mb-3">
                                <label class="small font-weight-bold text-muted">الاسم الكامل</label>
                                <input type="text" id="patientName" class="form-control" placeholder="مثال: سارة بنجلون" required style="height: 48px; border-radius: 8px;">
                            </div>
                            <div class="form-group mb-3">
                                <label class="small font-weight-bold text-muted">رقم الهاتف (واتساب)</label>
                                <input type="tel" id="patientPhone" class="form-control" placeholder="06XXXXXXXX" required style="height: 48px; border-radius: 8px;">
                            </div>
                            <div class="form-group mb-3">
                                <label class="small font-weight-bold text-muted">العلاج المطلوب</label>
                                <select id="treatmentType" class="form-control" style="height: 48px; border-radius: 8px;">
                                    <option value="علاج وادي الدموع والهالات">علاج وادي الدموع والهالات</option>
                                    <option value="استعادة امتلاء الخدود Pommettes">استعادة امتلاء الخدود Pommettes</option>
                                    <option value="تحديد الفك والذقن تكساس">تحديد الفك والذقن تكساس</option>
                                    <option value="فيلر وترطيب الشفاه الطبيعي">فيلر وترطيب الشفاه الطبيعي</option>
                                    <option value="بوتوكس تجاعيد الجبهة">بوتوكس تجاعيد الجبهة</option>
                                    <option value="سكين بوستر ونضارة البشرة">سكين بوستر ونضارة البشرة</option>
                                    <option value="استشارة وتشخيص عام للوجه">استشارة وتشخيص عام للوجه</option>
                                </select>
                            </div>
                            <div class="form-group mb-4">
                                <label class="small font-weight-bold text-muted">اليوم المفضل</label>
                                <input type="date" id="preferredDate" class="form-control" style="height: 48px; border-radius: 8px;">
                            </div>
                            <button type="submit" class="btn btn-block btn-gold font-weight-bold" style="height: 52px; font-size: 16px; border-radius: 8px;">
                                <i class="fab fa-whatsapp ml-2"></i> إرسال وتأكيد عبر واتساب
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section id="temoignages" class="py-5" style="background: #f8fafc;">
        <div class="container py-4">
            <div class="text-center max-w-700 mx-auto mb-5">
                <span class="text-uppercase text-gold font-weight-bold" style="font-size: 14px; letter-spacing: 1px;">آراء مريضاتنا</span>
                <h2 class="display-5 font-serif font-weight-bold mt-2" style="color: var(--primary-emerald);">تجارب حقيقية تعكس ثقة مريضاتنا</h2>
                <p class="text-muted">شهادات عفوية تعبر عن التزامنا بالنتيجة الطبيعية والتعامل الإنساني الراقي.</p>
            </div>

            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="treatment-card p-4">
                        <div class="text-warning mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-muted small" style="line-height: 1.7;">
                            "كنت خائفة جداً من أن يتغير شكلي أو يبدو وجهي منتفخاً. دكتورة حنان طمأنتني تماماً. الهالات السوداء اختفت وكل من يراني يقول إنني أبدو مرتاحة ونضرة كأنني عدت من عطلة!"
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div class="rounded-circle bg-emerald text-white d-flex align-items-center justify-content-center font-weight-bold ml-3" style="width: 42px; height: 42px;">
                                م.ك
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-dark">مريم ك.</h6>
                                <small class="text-muted">الدار البيضاء • وادي الدموع</small>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 mb-4">
                    <div class="treatment-card p-4">
                        <div class="text-warning mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-muted small" style="line-height: 1.7;">
                            "لمسة الدكتورة حنان فيها دقة عالية جداً. استطاعت رسم زاوية الفك بدون أي مبالغة. الإجراء بالميكرو-كانيل لم يكن مؤلماً إطلاقاً. طبيبة متمكنة جداً."
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div class="rounded-circle bg-gold text-white d-flex align-items-center justify-content-center font-weight-bold ml-3" style="width: 42px; height: 42px;">
                                ل.ع
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-dark">ليلى ع.</h6>
                                <small class="text-muted">الدار البيضاء • بروفايل تكساس</small>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 mb-4">
                    <div class="treatment-card p-4">
                        <div class="text-warning mb-2">
                            <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                        </div>
                        <p class="text-muted small" style="line-height: 1.7;">
                            "سعيدة جداً بالنتيجة! لم أعد بحاجة لتعديل صوري أو وضع فلاتر في سناب أو إنستغرام. النتيجة طبيعية وناعمة. شكراً جزيلاً دكتورة حنان على حسن تعاملك وموهبتك."
                        </p>
                        <div class="d-flex align-items-center mt-3 pt-3 border-top">
                            <div class="rounded-circle bg-emerald text-white d-flex align-items-center justify-content-center font-weight-bold ml-3" style="width: 42px; height: 42px;">
                                ز.ب
                            </div>
                            <div>
                                <h6 class="mb-0 font-weight-bold text-dark">زينب ب.</h6>
                                <small class="text-muted">الدار البيضاء • تناسق الملامح</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-5" style="background: #ffffff;">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <span class="text-uppercase text-gold font-weight-bold" style="font-size: 14px; letter-spacing: 1px;">العنوان والموقع</span>
                    <h2 class="display-5 font-serif font-weight-bold mt-2 mb-3" style="color: var(--primary-emerald);">العيادة الطبية بالدار البيضاء</h2>
                    <p class="text-muted mb-4" style="line-height: 1.8;">
                        بيئة راقية، خصوصية تامة، ومجهزة بأحدث التقنيات المعتمدة في طب التجميل.
                    </p>
                    <div class="d-flex mb-3">
                        <i class="fas fa-map-marked-alt text-gold ml-3 fa-lg mt-1"></i>
                        <div>
                            <h6 class="font-weight-bold mb-0 text-dark">عنوان العيادة</h6>
                            <p class="text-muted small">الدار البيضاء، المغرب (المواعيد مسبقة فقط)</p>
                        </div>
                    </div>
                    <div class="d-flex mb-3">
                        <i class="fas fa-phone-alt text-emerald ml-3 fa-lg mt-1"></i>
                        <div>
                            <h6 class="font-weight-bold mb-0 text-dark">الهاتف الثابت</h6>
                            <p class="text-muted small"><a href="tel:0520604484" class="text-dark font-weight-bold">05 20 60 44 84</a></p>
                        </div>
                    </div>
                    <div class="d-flex mb-3">
                        <i class="fab fa-whatsapp text-success ml-3 fa-lg mt-1"></i>
                        <div>
                            <h6 class="font-weight-bold mb-0 text-dark">واتساب وجوال</h6>
                            <p class="text-muted small"><a href="https://wa.me/212600980685" target="_blank" class="text-dark font-weight-bold">06 00 98 06 85</a></p>
                        </div>
                    </div>
                    <div class="d-flex">
                        <i class="fab fa-facebook-f text-primary ml-3 fa-lg mt-1"></i>
                        <div>
                            <h6 class="font-weight-bold mb-0 text-dark">الصفحة الرسمية على فيسبوك</h6>
                            <p class="text-muted small"><a href="https://web.facebook.com/people/Docteur-hanane-kashi/100091182893832/" target="_blank" class="text-primary font-weight-bold">Docteur hanane kashi</a></p>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6">
                    <div class="p-4 rounded-lg bg-light border text-center shadow-sm">
                        <div class="mb-3">
                            <i class="far fa-clock text-gold fa-3x"></i>
                        </div>
                        <h4 class="font-serif font-weight-bold text-dark mb-2">أوقات العمل</h4>
                        <p class="text-muted small mb-4">الاستشارات بموعد مسبق لضمان العناية التامة بكل مريضة دون أي انتظار.</p>
                        <div class="d-flex justify-content-between py-2 border-bottom">
                            <span class="font-weight-bold text-dark">الإثنين – الجمعة</span>
                            <span class="text-muted">09:30 – 18:30</span>
                        </div>
                        <div class="d-flex justify-content-between py-2 border-bottom">
                            <span class="font-weight-bold text-dark">السبت</span>
                            <span class="text-muted">09:30 – 14:00</span>
                        </div>
                        <div class="d-flex justify-content-between py-2">
                            <span class="font-weight-bold text-dark">الأحد</span>
                            <span class="text-danger font-weight-bold">مغلق</span>
                        </div>
                        <a href="https://wa.me/212600980685?text=السلام%20عليكم%20دكتورة%20حنان%20كاشي،%20أود%20معرفة%20الأوقات%20المتاحة%20للمواعيد." target="_blank" class="btn-whatsapp btn-block mt-4 justify-content-center">
                            <i class="fab fa-whatsapp"></i> الاستفسار عن الأوقات المتاحة
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-light py-4" style="background-color: #0b1e18 !important; border-top: 1px solid rgba(255,255,255,0.08);">
        <div class="container text-center text-md-right">
            <div class="row align-items-center">
                <div class="col-md-6 mb-3 mb-md-0 d-flex align-items-center justify-content-center justify-content-md-start">
                    <img src="assets/img/dr-kashi-logo.jpg" alt="شعار الدكتورة حنان كاشي" style="height: 44px; width: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #c5a059;" class="ml-3">
                    <div>
                        <h5 class="font-serif text-white mb-0">الدكتورة حنان كاشي</h5>
                        <p class="small text-muted mb-0">طب التجميل، الحقن والعناية بالبشرة بالدار البيضاء.</p>
                    </div>
                </div>
                <div class="col-md-6 text-center text-md-left">
                    <p class="small text-muted mb-0">
                        &copy; 2026 عيادة الدكتورة حنان كاشي. جميع الحقوق محفوظة. <br>
                        تم التطوير لتقديم أفضل تجربة مريضة ممكنة.
                    </p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Floating WhatsApp -->
    <a href="https://wa.me/212600980685?text=السلام%20عليكم%20دكتورة%20حنان%20كاشي،%20أود%20حجز%20موعد%20استشارة." target="_blank" class="floating-whatsapp" aria-label="واتساب الدكتورة حنان كاشي">
        <i class="fab fa-whatsapp"></i>
    </a>

    <!-- Sticky Mobile Contact Bar -->
    <div class="sticky-mobile-bar">
        <a href="tel:0520604484" class="sticky-call">
            <i class="fas fa-phone-alt"></i> 05 20 60 44 84
        </a>
        <a href="https://wa.me/212600980685?text=السلام%20عليكم%20دكتورة%20حنان%20كاشي،%20أود%20حجز%20موعد%20استشارة." target="_blank" class="sticky-wa">
            <i class="fab fa-whatsapp"></i> واتساب
        </a>
    </div>

    <!-- Scripts -->
    <script src="assets/js/jquery-1.12.4.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/bootsnav.js"></script>
    <script>
        function handleAppointmentSubmit(e) {
            e.preventDefault();
            var name = document.getElementById('patientName').value.trim();
            var phone = document.getElementById('patientPhone').value.trim();
            var treatment = document.getElementById('treatmentType').value;
            var date = document.getElementById('preferredDate').value;

            var msg = "السلام عليكم دكتورة حنان كاشي،%0A%0Aأود حجز موعد استشارة :%0A" +
                      "• الاسم : " + encodeURIComponent(name) + "%0A" +
                      "• الهاتف : " + encodeURIComponent(phone) + "%0A" +
                      "• العلاج المطلوب : " + encodeURIComponent(treatment);
            if (date) {
                msg += "%0A• التاريخ المفضل : " + encodeURIComponent(date);
            }
            msg += "%0A%0Aيرجى تأكيد الموعد المناسب.";

            window.open("https://wa.me/212600980685?text=" + msg, "_blank");
        }
    </script>
</body>
</html>
"""
    return head + body

def main():
    fr_html = generate_french_page()
    ar_html = generate_arabic_page()

    fr_path = CLINIC_DIR / "index.html"
    ar_path = CLINIC_DIR / "ar.html"

    fr_path.write_text(fr_html, encoding="utf-8")
    ar_path.write_text(ar_html, encoding="utf-8")

    print(f"✅ Generated French version at: {fr_path} ({len(fr_html)} chars)")
    print(f"✅ Generated Arabic version at: {ar_path} ({len(ar_html)} chars)")

if __name__ == "__main__":
    main()
