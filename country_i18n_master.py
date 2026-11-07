# -*- coding: utf-8 -*-
"""
Full native dictionary with all 21 languages unified with all sections:
- Nav header
- Hero (H1 in 3 lines)
- Why choose Save My Play (exact 3 reasons)
- Pricing table (3 rows matching the requested pricing model: 180 HW, 45 Recording, 136 AI)
- Real Court Demonstration (4 videos with responsive grid)
- Collapsible FAQs (<details><summary>)
- Direct Contact Cards (WhatsApp with QR + Email with QR)
- Full Textured-Blue Footer with 4 SEO silos and legal links
"""

from country_i18n_unified import ALL_LANGS_UNIFIED

# We import the base 21 languages from ALL_LANGS_I18N and enrich them with the video/faq/footer/contact fields
from country_i18n_dict_full import ALL_LANGS_I18N

# Default English fallback additions for any secondary language keys
EN_EXTRA = {
    "pricing_th_plan": "Plan / Specification", "pricing_th_invest": "Investment / Fee", "pricing_th_mod": "Terms", "pricing_th_serv": "Included Features",
    "tbl_hw_title": "Hardware Investment (Owned)", "tbl_hw_mod": "One-time payment", "tbl_hw_desc": "1 rectilinear sports camera per court (no fish-eye distortion) + security post mount",
    "tbl_rec_title": "Match Recording, Highlights & Streaming", "tbl_rec_mod": "0 lock-in • Month-to-month", "tbl_rec_desc": "Private cloud recording, instant mobile highlights, and official YouTube live streaming with club branding",
    "tbl_ai_title": "AI Match Statistics & Tactical Analysis", "tbl_ai_mod": "0 lock-in • Optional", "tbl_ai_desc": "Shot breakdown, court heatmaps, ball speed tracking, and individual player performance analytics",
    "pricing_footnote": "* Prices exclude VAT. Zero contract lock-in. 5-minute setup.",

    "vid_badge": "Real Court Demonstration",
    "vid_title": "Experience Recording and Streaming Quality",
    "vid_sub": "Official FIP live broadcasts, automated highlights, and tactical coaching analysis tools.",
    "vid1_t": "FIP Miami Padel Open", "vid1_d": "Official live stream and multi-court broadcasting",
    "vid2_t": "Automated Match Highlights", "vid2_d": "Direct mobile QR download without installing apps",
    "vid3_t": "Tactical Coaching Video", "vid3_d": "Performance analysis tools for coaches and academies",
    "vid4_t": "Club Tournament Broadcast", "vid4_d": "YouTube live streaming with club branding overlay",

    "faq_title": "Frequently Asked Questions",
    "faq_sub": "Everything you need to know about Save My Play camera system for padel clubs",
    "faq1_q": "Are civil works, cabling, or floor trenches required?",
    "faq1_a": "No, absolutely zero works. The camera mounts directly onto the court net post or light column in just 5 minutes.",
    "faq2_q": "What is the pricing model and what plans exist?",
    "faq2_a": "{hw} per camera owned outright. Monthly subscriptions: {rec} per court for recording, highlights, and live streaming; or {ai} for AI statistics and tactical analysis.",
    "faq3_q": "How does the AI process the best shots?",
    "faq3_a": "The cameras use AI to process the video stream in real time, automatically extracting top rallies ready to share on mobile.",
    "faq4_q": "Is there any long-term contract or lock-in?",
    "faq4_a": "Zero contract lock-in. Cancel or pause month-to-month without penalty.",

    "contact_badge": "Direct Contact", "contact_title": "Contact Us", "contact_sub": "Fast response for club managers, tournaments, and live demos.",
    "contact_wa_btn": "Send WhatsApp", "contact_mail_btn": "Send Email",

    "footer_b2b": "B2B Solutions", "footer_tech": "Court Technology", "footer_tools": "Free Tools", "footer_corp": "Corporate & Legal"
}

ALL_LANGS_MASTER = {}

for lang_code, base_dict in ALL_LANGS_I18N.items():
    if lang_code in ALL_LANGS_UNIFIED:
        # Merge unified
        merged = dict(base_dict)
        merged.update(ALL_LANGS_UNIFIED[lang_code])
        ALL_LANGS_MASTER[lang_code] = merged
    else:
        # Enrich with EN_EXTRA
        merged = dict(base_dict)
        for k, v in EN_EXTRA.items():
            if k not in merged:
                merged[k] = v
        ALL_LANGS_MASTER[lang_code] = merged

print(f"ALL_LANGS_MASTER compiled with {len(ALL_LANGS_MASTER)} fully unified languages.")
