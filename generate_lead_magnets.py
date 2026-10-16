#!/usr/bin/env python3
"""
Generador de Lead Magnets Reales (Excel y PDFs) para CoolPadel Studios & Save my Play.
Crea:
1. coolpadel-web/assets/downloads/calculadora-roi-camaras-padel.xlsx
2. coolpadel-web/assets/downloads/checklist-organizacion-torneos-padel.pdf
3. coolpadel-web/assets/downloads/cartel-homologado-rgpd-pistas-padel.pdf
4. coolpadel-web/assets/downloads/protocolo-smart-court-horas-valle.pdf
"""
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from fpdf import FPDF

OUT_DIR = os.path.join(os.path.dirname(__file__), "assets", "downloads")
os.makedirs(OUT_DIR, exist_ok=True)

# ==========================================
# 1. EXCEL: CALCULADORA DE AMORTIZACIÓN Y ROI
# ==========================================
def generate_excel_roi():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Calculadora ROI Cámaras"
    ws.views.sheetView[0].showGridLines = True

    # Paleta de colores
    header_fill = PatternFill(start_color="0B1626", end_color="0B1626", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    accent_fill = PatternFill(start_color="F2920B", end_color="F2920B", fill_type="solid")
    accent_font = Font(name="Calibri", size=11, bold=True, color="000000")
    section_fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    section_font = Font(name="Calibri", size=11, bold=True, color="0B1626")
    total_fill = PatternFill(start_color="E2E8F0", end_color="E2E8F0", fill_type="solid")
    total_font = Font(name="Calibri", size=12, bold=True, color="0B1626")
    profit_font = Font(name="Calibri", size=13, bold=True, color="166534")

    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )

    # Título principal
    ws.merge_cells("A1:E1")
    ws["A1"] = "SAVE MY PLAY - CALCULADORA DE AMORTIZACIÓN Y ROI PARA CLUBES DE PÁDEL"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = header_fill
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 35

    ws.merge_cells("A2:E2")
    ws["A2"] = "Simulador oficial de ingresos, cuotas mensuales y amortización de hardware sin permanencia"
    ws["A2"].font = Font(name="Calibri", size=10, italic=True, color="64748B")
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 20

    # SECCIÓN 1: PARÁMETROS DEL CLUB
    ws["A4"] = "1. PARÁMETROS BÁSICOS DEL CLUB"
    ws["A4"].font = section_font
    ws.merge_cells("A4:E4")
    ws["A4"].fill = section_fill

    params = [
        ("Número de pistas a equipar con cámara", 4, "pistas", "Modifica este valor (ej. 2, 4, 8)"),
        ("Partidos disputados al mes por pista", 80, "partidos/mes", "Media habitual (3 a 4 turnos/día x 25 días)"),
        ("Precio del hardware Save my Play por pista", 180, " EUR (pago único)", "Hardware en propiedad (cámara panorámica HD + poste)"),
        ("Cuota mensual software Save my Play (Plan B)", 45, " EUR/mes por pista", "Grabación, replays con botón en poste, YouTube y QR"),
    ]

    for i, (desc, val, unit, note) in enumerate(params, start=5):
        ws.row_dimensions[i].height = 22
        ws[f"A{i}"] = desc
        ws[f"B{i}"] = val
        ws[f"C{i}"] = unit
        ws[f"D{i}"] = note
        ws[f"A{i}"].font = Font(bold=(i == 5))
        ws[f"B{i}"].font = Font(bold=True)
        ws[f"B{i}"].alignment = Alignment(horizontal="right")
        ws[f"C{i}"].font = Font(color="64748B")
        ws[f"D{i}"].font = Font(italic=True, color="94A3B8")
        for col in ["A", "B", "C", "D"]:
            ws[f"{col}{i}"].border = thin_border

    # SECCIÓN 2: MODELOS DE MONETIZACIÓN (ELIGE O COMBINA)
    ws["A10"] = "2. INGRESOS ESTIMADOS SEGÚN MODELO DE EXPLOTACIÓN"
    ws["A10"].font = section_font
    ws.merge_cells("A10:E10")
    ws["A10"].fill = section_fill

    ws["A11"] = "Concepto de Ingreso"
    ws["B11"] = "Importe Unitario"
    ws["C11"] = "Volumen / Adopción"
    ws["D11"] = "Ingreso Mensual Total ( EUR)"
    ws["E11"] = "Notas operativas"
    for col in ["A", "B", "C", "D", "E"]:
        ws[f"{col}11"].font = header_font
        ws[f"{col}11"].fill = header_fill
        ws[f"{col}11"].alignment = Alignment(horizontal="center")

    modelos = [
        ("Modelo 1: Cobro directo por descarga (1 EUR/jugador)", 1.0, "30% de los partidos (4 jugadores)", "=B5*B6*0.30*4*B12", "Los jugadores pagan 1 EUR por tener el vídeo completo y clips"),
        ("Modelo 2: Recargo en reserva de pista con cámara", 1.0, "50% de las reservas", "=B5*B6*0.50*B13", "El club incrementa 1 EUR/hora en pistas equipadas"),
        ("Modelo 3: Patrocinador local por pista (pantallas/postes)", 75.0, "=B5", "=B5*B14", "Una empresa local patrocina la pista y los vídeos"),
    ]

    for idx, (m_desc, m_val, m_vol, m_formula, m_note) in enumerate(modelos, start=12):
        ws.row_dimensions[idx].height = 24
        ws[f"A{idx}"] = m_desc
        ws[f"B{idx}"] = m_val
        ws[f"C{idx}"] = m_vol
        ws[f"D{idx}"] = m_formula
        ws[f"E{idx}"] = m_note
        ws[f"B{idx}"].number_format = '#,##0.00  EUR'
        ws[f"D{idx}"].number_format = '#,##0.00  EUR'
        ws[f"D{idx}"].font = Font(bold=True)
        for col in ["A", "B", "C", "D", "E"]:
            ws[f"{col}{idx}"].border = thin_border

    # SECCIÓN 3: CUENTA DE RESULTADOS Y AMORTIZACIÓN
    ws["A16"] = "3. RESUMEN FINANCIERO MENSUAL Y RETORNO DE INVERSIÓN (ROI)"
    ws["A16"].font = section_font
    ws.merge_cells("A16:E16")
    ws["A16"].fill = section_fill

    resumen = [
        ("Inversión inicial total en hardware (en propiedad)", "=B5*B7", "Pago único sin permanencia"),
        ("Coste mensual total del software Save my Play", "=B5*B8", "Cuota mensual recurrente"),
        ("Ingresos mensuales estimados (aplicando Modelo 2 + Patrocinio)", "=D13+D14", "Suma de reservas + sponsor"),
        ("BENEFICIO NETO MENSUAL PARA EL CLUB", "=B19-B18", "Beneficio directo recurrente"),
        ("PLAZO DE AMORTIZACIÓN DE LA INVERSIÓN (PAYBACK)", "=B17/B20", "Meses necesarios para recuperar el 100%"),
    ]

    for i, (r_desc, r_formula, r_note) in enumerate(resumen, start=17):
        ws.row_dimensions[i].height = 26
        ws[f"A{i}"] = r_desc
        ws[f"B{i}"] = r_formula
        ws[f"C{i}"] = r_note
        ws[f"A{i}"].font = Font(bold=(i >= 20))
        ws[f"B{i}"].font = Font(bold=True, size=11)
        if i in [17, 18, 19]:
            ws[f"B{i}"].number_format = '#,##0.00  EUR'
        elif i == 20:
            ws[f"A{i}"].fill = accent_fill
            ws[f"B{i}"].fill = accent_fill
            ws[f"B{i}"].font = profit_font
            ws[f"B{i}"].number_format = '#,##0.00  EUR'
        elif i == 21:
            ws[f"A{i}"].fill = total_fill
            ws[f"B{i}"].fill = total_fill
            ws[f"B{i}"].font = total_font
            ws[f"B{i}"].number_format = '0.0 "meses"'
        for col in ["A", "B", "C"]:
            ws[f"{col}{i}"].border = thin_border

    # SECCIÓN 4: INFORMACIÓN DE CONTACTO / DEMO
    ws["A23"] = "💡 ¿Quieres probar las cámaras en tu club o validar estos números con Javier Villoria?"
    ws["A23"].font = Font(bold=True, color="0B1626")
    ws.merge_cells("A23:E23")

    ws["A24"] = "WhatsApp directo: +34 680 31 74 86 | Email: javier@coolpadelstudios.com | Web: https://coolpadelstudios.com/camaras/"
    ws["A24"].font = Font(italic=True, color="2563EB")
    ws.merge_cells("A24:E24")

    # Ajuste de ancho de columnas
    ws.column_dimensions["A"].width = 54
    ws.column_dimensions["B"].width = 24
    ws.column_dimensions["C"].width = 34
    ws.column_dimensions["D"].width = 28
    ws.column_dimensions["E"].width = 46

    excel_path = os.path.join(OUT_DIR, "calculadora-roi-camaras-padel.xlsx")
    wb.save(excel_path)
    print(f"  [OK] Excel generado: {excel_path}")


# ==========================================
# 2. PDF: CHECKLIST OFICIAL ORGANIZACIÓN TORNEOS
# ==========================================
class CoolPadelPDF(FPDF):
    def header(self):
        self.set_fill_color(11, 22, 38)
        self.rect(0, 0, 210, 18, 'F')
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(242, 146, 11)
        self.set_xy(10, 4)
        self.cell(0, 10, 'COOLPADEL STUDIOS - DOCUMENTO DE GESTIÓN Y OPERACIONES B2B', 0, 0, 'L')
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', '', 8)
        self.set_xy(10, 4)
        self.cell(190, 10, 'coolpadelstudios.com', 0, 0, 'R')
        self.ln(18)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, f'Página {self.page_no()} | Guía práctica de Torneos de Pádel - Javier Villoria', 0, 0, 'C')

def generate_pdf_torneos():
    pdf = CoolPadelPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # Título del documento
    pdf.set_font('Helvetica', 'B', 18)
    pdf.set_text_color(11, 22, 38)
    pdf.cell(0, 10, 'Checklist Oficial de Organización de Torneos de Pádel', 0, 1, 'L')
    pdf.set_font('Helvetica', 'I', 10)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 6, 'Cronograma, Welcome Packs Memorables y Rentabilización con Patrocinadores', 0, 1, 'L')
    pdf.ln(5)

    # Introducción
    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 5, 'Organizar un torneo de pádel rentable y bien valorado requiere evitar los errores comunes: camisetas técnicas baratas que nadie usa, falta de previsión de bolas y sobrecostes imprevistos. Utiliza esta lista de verificación para controlar cada fase del evento.')
    pdf.ln(4)

    # Bloque 1: Cronograma -6 semanas
    def draw_section(title, items):
        pdf.set_fill_color(241, 245, 249)
        pdf.set_font('Helvetica', 'B', 11)
        pdf.set_text_color(11, 22, 38)
        pdf.cell(0, 8, f'  {title}', 0, 1, 'L', fill=True)
        pdf.ln(2)
        pdf.set_font('Helvetica', '', 9)
        pdf.set_text_color(51, 65, 85)
        for box, text in items:
            pdf.cell(6, 5, '[ ]', 0, 0, 'L')
            pdf.multi_cell(0, 5, f'{box}: {text}')
            pdf.ln(1)
        pdf.ln(3)

    draw_section('FASE 1: 6 SEMANAS ANTES (PLANIFICACIÓN & PATROCINADORES)', [
        ('Definición de Categorías y Límite de Parejas', 'Establecer cuadros (1ª, 2ª, 3ª masculina/femenina/mixta) y número de pistas disponibles.'),
        ('Diseño y Muestra del Llavero 3D', 'Solicitar la muestra física a CoolPadel Studios (15 EUR, 100% deducible). Cara A con logo del torneo, Cara B reservada para el patrocinador principal.'),
        ('Venta de Patrocinio del Welcome Pack', 'Presentar la muestra física real en mano al concesionario o negocio local. Cierra 400 EUR - 800 EUR fácilmente al asegurar presencia diaria en paleteros.'),
        ('Apertura de Inscripciones', 'Configurar pasarela de pago o software (Playtomic, Matchi, etc.) y publicar el cartel en redes y tablones.')
    ])

    draw_section('FASE 2: 3 SEMANAS ANTES (PRODUCCIÓN & SUMINISTROS)', [
        ('Confirmación de Tirada de Merchandising', 'Confirmar unidades exactas de llaveros de goma 3D (desde 100 uds) y envíos con CoolPadel Studios.'),
        ('Compra de Consumibles Deportivos', 'Pedir overgrips microperforados y botes de bolas (Head Padel Pro / Bullpadel) calculando 1 bote por partido de cuadro.'),
        ('Bolsas y Packaging Ecológico', 'Bolsas de papel kraft personalizadas con sello del club o tarjeta de bienvenida.')
    ])

    draw_section('FASE 3: 1 SEMANA ANTES (CUADROS & LOGÍSTICA DE PISTA)', [
        ('Sorteo de Cuadros y Publicación de Horarios', 'Publicar horarios de primera ronda avisando a jugadores por email y WhatsApp.'),
        ('Montaje de Cámaras y Retransmisión', 'Revisar cámara Save my Play en pista central para emitir semifinales y finales en directo en YouTube.'),
        ('Montaje de Welcome Packs', 'Embolsar llavero 3D, overgrip, agua/isotónico y tarjeta de descuentos de sponsors.')
    ])

    draw_section('FASE 4: DÍA DEL TORNEO & ENTREGA DE PREMIOS', [
        ('Mesa de Control y Check-in', 'Entrega de welcome pack nominativo al recibir a cada pareja en recepción.'),
        ('Árbitro y Gestión de Resultados', 'Actualización en vivo de clasificaciones y avisos de pista.'),
        ('Finales y Photocall Oficial', 'Retransmisión en streaming de las finales y fotos de los campeones y subcampeones en el podio con sus llaveros oficiales.')
    ])

    pdf.set_fill_color(254, 243, 199)
    pdf.rect(10, pdf.get_y(), 190, 20, 'F')
    pdf.set_xy(12, pdf.get_y() + 3)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_text_color(180, 83, 9)
    pdf.cell(0, 5, '¿NECESITAS LOS LLAVEROS OFICIALES O CÁMARAS PARA TU TORNEO?', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(11, 22, 38)
    pdf.cell(0, 5, 'Escribe directamente a Javier Villoria: +34 680 31 74 86 | javier@coolpadelstudios.com', 0, 1, 'L')

    torneo_pdf_path = os.path.join(OUT_DIR, "checklist-organizacion-torneos-padel.pdf")
    pdf.output(torneo_pdf_path)
    print(f"  [OK] PDF Torneos generado: {torneo_pdf_path}")


# ==========================================
# 3. PDF: CARTEL HOMOLOGADO RGPD PARA PISTAS
# ==========================================
def generate_pdf_cartel_rgpd():
    pdf = CoolPadelPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Cabecera tipo cartel homologado
    pdf.set_fill_color(11, 22, 38)
    pdf.rect(10, 25, 190, 28, 'F')
    pdf.set_xy(10, 27)
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(242, 146, 11)
    pdf.cell(190, 8, 'ZONA DEPORTIVA VIDEODOCUMENTADA', 0, 1, 'C')
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(190, 6, 'INFORMACIÓN BÁSICA SOBRE PROTECCIÓN DE DATOS (RGPD UE 2016/679 - LOPDGDD 3/2018)', 0, 1, 'C')
    pdf.ln(12)

    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 5, 'En cumplimiento del Reglamento General de Protección de Datos (UE) 2016/679 y la Ley Orgánica 3/2018 de Protección de Datos Personales y garantía de los derechos digitales, se informa a los usuarios de las instalaciones de lo siguiente:')
    pdf.ln(5)

    def draw_rgpd_row(label, content):
        pdf.set_fill_color(241, 245, 249)
        pdf.set_font('Helvetica', 'B', 9.5)
        pdf.set_text_color(11, 22, 38)
        pdf.cell(50, 9, f' {label}', 1, 0, 'L', fill=True)
        pdf.set_font('Helvetica', '', 9)
        pdf.set_text_color(51, 65, 85)
        pdf.multi_cell(140, 9, f' {content}', 1, 'L')

    draw_rgpd_row('Responsable del Tratamiento', 'Club Deportivo / Titular de la Instalación Deportiva (Ver datos en Recepción).')
    draw_rgpd_row('Tecnología de Grabación', 'Sistema Save my Play (CoolPadel Studios). Cámara cenital de ámbito deportivo.')
    draw_rgpd_row('Finalidad del Tratamiento', 'Captura de puntos deportivos destacados a solicitud voluntaria del propio jugador mediante pulsador físico en pista y retransmisión de eventos.')
    draw_rgpd_row('Legitimación', 'Interés legítimo en la prestación de servicios deportivos y consentimiento explícito al activar el pulsador de grabación.')
    draw_rgpd_row('Conservación de Imágenes', 'Buffer circular de 25 segundos en memoria temporal local. Los clips descargados se suprimen automáticamente según la política de caducidad del sistema (máx. 30 días).')
    draw_rgpd_row('Destinatarios y Cesión', 'No se cederán datos a terceros salvo obligación legal. Las imágenes solicitadas solo son accesibles por los propios jugadores que escanean el código QR en pista.')
    draw_rgpd_row('Derechos del Interesado', 'Acceso, rectificación, supresión y oposición dirigiendo escrito a la dirección postal del club o ante la Agencia Española de Protección de Datos (aepd.es).')

    pdf.ln(6)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(11, 22, 38)
    pdf.cell(0, 6, 'AVISO PARA JUGADORES Y ACOMPAÑANTES:', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(71, 85, 105)
    pdf.multi_cell(0, 4.5, 'Este sistema NO constituye videovigilancia de seguridad. Su único propósito es la asistencia técnica deportiva y el entretenimiento de los jugadores en pista. Si no desea que sus jugadas queden registradas, basta con no accionar el pulsador de replay situado junto a la red.')

    pdf.ln(6)
    # Espacio para sello del club
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(10, pdf.get_y(), 90, 30)
    pdf.set_xy(12, pdf.get_y() + 2)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.cell(86, 5, 'Razón Social del Club / Instalación Deportiva:', 0, 1, 'L')
    pdf.cell(86, 5, 'NIF / CIF:', 0, 1, 'L')
    pdf.cell(86, 5, 'Email de contacto DPD / Privacidad:', 0, 1, 'L')

    pdf.set_xy(110, pdf.get_y() - 17)
    pdf.rect(110, pdf.get_y(), 90, 30)
    pdf.set_xy(112, pdf.get_y() + 2)
    pdf.cell(86, 5, 'Sello / Firma del Responsable del Club:', 0, 1, 'L')

    cartel_pdf_path = os.path.join(OUT_DIR, "cartel-homologado-rgpd-pistas-padel.pdf")
    pdf.output(cartel_pdf_path)
    print(f"  [OK] PDF Cartel RGPD generado: {cartel_pdf_path}")


# ==========================================
# 4. PDF: PROTOCOLO SMART COURTS & HORAS VALLE
# ==========================================
def generate_pdf_smart_courts():
    pdf = CoolPadelPDF()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()

    pdf.set_font('Helvetica', 'B', 18)
    pdf.set_text_color(11, 22, 38)
    pdf.cell(0, 10, 'Protocolo de Pistas Inteligentes (Smart Courts)', 0, 1, 'L')
    pdf.set_font('Helvetica', 'I', 10)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 6, 'Estrategia Operativa para Rentabilizar Horas Valle (10:00 - 17:00) en Clubes de Pádel', 0, 1, 'L')
    pdf.ln(5)

    pdf.set_font('Helvetica', '', 9.5)
    pdf.set_text_color(30, 41, 59)
    pdf.multi_cell(0, 5, 'El mayor desafío de un club de pádel no es llenar las pistas de 18:00 a 22:00, sino rentabilizar la inversión fija en las horas muertas de la mañana. Una pista inteligente combina domótica, grabación Save my Play y formatos comerciales específicos para aumentar la ocupación matinal del 15% al 55%.')
    pdf.ln(4)

    def draw_smart_pillar(num, title, bullets):
        pdf.set_fill_color(241, 245, 249)
        pdf.set_font('Helvetica', 'B', 11)
        pdf.set_text_color(11, 22, 38)
        pdf.cell(0, 8, f'  PILAR {num}: {title}', 0, 1, 'L', fill=True)
        pdf.ln(2)
        pdf.set_font('Helvetica', '', 9)
        pdf.set_text_color(51, 65, 85)
        for b in bullets:
            pdf.cell(5, 5, '-', 0, 0, 'L')
            pdf.multi_cell(0, 5, b)
            pdf.ln(1)
        pdf.ln(3)

    draw_smart_pillar(1, 'DOMÓTICA Y EFICIENCIA ENERGÉTICA SIN OBRA', [
        'Automatización de iluminación LED vinculada a la reserva: la pista solo enciende luces cuando hay jugadores dentro.',
        'Apertura de accesos mediante cerradura inteligente (código PIN o QR), permitiendo turnos matinales sin personal dedicado en recepción.',
        'Ahorro estimado en factura de electricidad: 180 EUR a 320 EUR al mes por cada 4 pistas.'
    ])

    draw_smart_pillar(2, 'CLINICS DE VÍDEO-ANÁLISIS MATINAL CON MONITORES', [
        'Los entrenadores del club utilizan las cámaras Save my Play para clases de tecnificación individual o en pareja.',
        'El monitor graba saques, bandejas y voleas con el pulsador en red y repasa el clip en cámara lenta con el alumno en una tablet.',
        'Permite cobrar un recargo de 10 EUR a 15 EUR por clase técnica matinal respecto a una clase convencional.'
    ])

    draw_smart_pillar(3, 'LIGAS EXPRESS MATINALES PARA TELETRABAJADORES Y JUBILADOS', [
        'Formato americano de 90 minutos de 10:00 a 11:30 o de 13:00 a 14:30.',
        'Incentivo del replay: los participantes descargan sus mejores jugadas al instante y las comparten en grupos de WhatsApp del club.',
        'Precio cerrado con consumición o menú saludable en la cafetería del club.'
    ])

    draw_smart_pillar(4, 'MONETIZACIÓN Y AMORTIZACIÓN EN MENOS DE 90 DÍAS', [
        'Inversión hardware Save my Play: 180 EUR por pista en propiedad.',
        'Cuota de software: 45 EUR al mes por pista sin permanencia.',
        'Con solo 3 alumnos de vídeo-análisis o un patrocinador local de 60 EUR/mes, la pista inteligente genera beneficio neto.'
    ])

    pdf.set_fill_color(242, 146, 11)
    pdf.rect(10, pdf.get_y(), 190, 18, 'F')
    pdf.set_xy(12, pdf.get_y() + 3)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(11, 22, 38)
    pdf.cell(0, 5, '¿QUIERES AUDITAR LA OCUPACIÓN DE TU CLUB Y MONTAR SMART COURTS?', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 8.5)
    pdf.set_text_color(11, 22, 38)
    pdf.cell(0, 5, 'Pide una auditoría online gratuita de 15 minutos con Javier Villoria: +34 680 31 74 86 | javier@coolpadelstudios.com', 0, 1, 'L')

    smart_pdf_path = os.path.join(OUT_DIR, "protocolo-smart-court-horas-valle.pdf")
    pdf.output(smart_pdf_path)
    print(f"  [OK] PDF Smart Courts generado: {smart_pdf_path}")


if __name__ == "__main__":
    print(">> Generando recursos y lead magnets descargables...")
    generate_excel_roi()
    generate_pdf_torneos()
    generate_pdf_cartel_rgpd()
    generate_pdf_smart_courts()
    print(">> ¡Todos los lead magnets generados con éxito en coolpadel-web/assets/downloads/!")
