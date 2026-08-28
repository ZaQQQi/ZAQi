#!/usr/bin/env python3
"""Generate PDF summary of the Aug 28 market review."""

from fpdf import FPDF
from pathlib import Path

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
OUTPUT = Path("/workspace/obzor-rynka-28-avg-2026.pdf")


class ReviewPDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "Обзор рынка — 28 августа 2026", align="R", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Стр. {self.page_no()}", align="C")

    def section_title(self, title: str):
        self.ln(4)
        self.set_font("DejaVu", "B", 14)
        self.set_text_color(20, 60, 120)
        w = self.w - self.l_margin - self.r_margin
        self.multi_cell(w, 8, title)
        self.ln(2)

    def sub_title(self, title: str):
        self.ln(2)
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(40, 40, 40)
        w = self.w - self.l_margin - self.r_margin
        self.multi_cell(w, 7, title)
        self.ln(1)

    def body(self, text: str):
        self.set_font("DejaVu", "", 10)
        self.set_text_color(30, 30, 30)
        w = self.w - self.l_margin - self.r_margin
        self.multi_cell(w, 5.5, text)
        self.ln(1)

    def bullet(self, text: str):
        self.set_font("DejaVu", "", 10)
        self.set_text_color(30, 30, 30)
        w = self.w - self.l_margin - self.r_margin
        x = self.get_x()
        self.cell(5, 5.5, "•")
        self.multi_cell(w - 5, 5.5, text)
        self.set_x(x)

    def code_block(self, text: str):
        self.set_font("DejaVu", "", 8.5)
        self.set_fill_color(245, 245, 245)
        self.set_text_color(20, 20, 20)
        w = self.w - self.l_margin - self.r_margin
        for line in text.split("\n"):
            self.cell(w, 5, line, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def table_header(self, cols, widths):
        self.set_font("DejaVu", "B", 9)
        self.set_fill_color(230, 240, 250)
        self.set_text_color(20, 20, 20)
        for col, w in zip(cols, widths):
            self.cell(w, 7, col, border=1, fill=True)
        self.ln()

    def table_row(self, cols, widths, bold_first=False):
        self.set_font("DejaVu", "B" if bold_first else "", 8)
        self.set_text_color(30, 30, 30)
        for i, (col, w) in enumerate(zip(cols, widths)):
            if i == 0:
                self.set_font("DejaVu", "B", 8)
            else:
                self.set_font("DejaVu", "", 8)
            self.cell(w, 6, col, border=1)
        self.ln()


def build_pdf():
    pdf = ReviewPDF()
    pdf.set_margins(12, 12, 12)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font("DejaVu", "", FONT)
    pdf.add_font("DejaVu", "B", FONT_BOLD)
    pdf.add_page()

    usable = pdf.w - pdf.l_margin - pdf.r_margin

    pdf.set_font("DejaVu", "B", 18)
    pdf.set_text_color(15, 45, 90)
    pdf.multi_cell(usable, 10, "Обзор рынка криптовалют и акций")
    pdf.set_font("DejaVu", "", 11)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(usable, 6, "28 августа 2026")
    pdf.multi_cell(usable, 6, "Источник: YouTube IMrq4m-YcYI")
    pdf.ln(3)

    pdf.section_title("Главный контекст дня")
    pdf.bullet("17:00 — выступление главы ФРС Кевина Уорша (Jackson Hole).")
    pdf.bullet("Слабые данные по инфляции на этой неделе.")
    pdf.bullet("Hawkish-риторика → откат BTC ко 2-й части сценария (76 250$).")
    pdf.bullet("Трамп: пошлины на полупроводники не из США. Бенефициары: Intel, Micron.")

    pdf.section_title("1. Bitcoin — сценарий и уровни")
    pdf.sub_title("Этапы сценария")
    pdf.code_block(
        "Этап 1 [OK]  Задёрг 79 800 – 80 250  (стопы локальных шортов)\n"
        "Этап 2 [>>]  Откат к 76 250           (лонговая ликвидность)\n"
        "Этап 3 [??]  Рост выше 83 000         (недельная шорт-ликвидность)"
    )

    pdf.sub_title("Ключевые уровни")
    w = [38, 38, 28, 76]
    pdf.table_header(["Уровень", "Роль", "Статус", "Действие"], w)
    rows = [
        ("79 800–80 250", "Стопы шортов", "Отработано", "Реакция продавца"),
        ("77 676–76 250", "Лонг-ликвидность", "Цель", "Возможен покупатель"),
        ("76 250", "Ключ. поддержка", "Вход", "Лонг (спот / 1–3x)"),
        ("> 83 000", "Шорт-ликвидность", "Цель вверх", "Пока не снята"),
    ]
    for r in rows:
        pdf.table_row(r, w)

    pdf.ln(2)
    pdf.sub_title("Схема движения BTC")
    pdf.code_block(
        "89k ─────────────────────────────\n"
        "83k ═════════════════════════════  <- шорт-ликвидность (цель)\n"
        "80k ----╮  [OK] задёрг 79.8–80.25\n"
        "       |\n"
        "76k ----┴──────────────────────  <- ЛОНГ (спот / плечо 1–3x)\n"
        "73k ───────────────────────────  (критич. уровень из прошл. обзора)"
    )

    pdf.sub_title("Точки входа по крипте (при BTC ~76 250$)")
    w2 = [24, 38, 22, 86]
    pdf.table_header(["Актив", "Условие", "Тип", "Комментарий"], w2)
    for r in [
        ("HYPE", "BTC ~76 250", "Long", "Раннер отскока"),
        ("PUMP", "BTC ~76 250", "Long", "Раннер отскока"),
        ("ZEC", "При падении BTC", "Long", "Зона на графике в моменте"),
    ]:
        pdf.table_row(r, w2)

    pdf.body(
        "Логика: пока 83k не снят, локальные откаты BTC — зона для спекуляций. "
        "FOMO рано: BTC всё ещё проигрывает по доходности за год."
    )

    pdf.section_title("2. Нефть — график и входы")
    pdf.sub_title("Brent (долгосрочный лонг)")
    pdf.bullet("Позиция: лонг с плечом 1–2x.")
    pdf.bullet("Цель: 98–102$ (недельная шорт-ликвидность).")
    pdf.bullet("Триггер: геополитическая эскалация (Иран, Ормузский пролив).")
    pdf.code_block(
        "102$ ═══════════════════  <- цель\n"
        " 98$ ═══════════════════\n"
        "     |\n"
        "  тек  <- держать лонг 1–2x"
    )

    pdf.sub_title("CL — американская нефть (лимитные ордера)")
    w3 = [22, 28, 130]
    pdf.table_header(["Уровень", "Тип", "Комментарий"], w3)
    for r in [
        ("69,2$", "Лимит long", "Если админ. погасит рост перед midterms"),
        ("66,2$", "Лимит long", "Глубокий откат — сильная точка входа"),
    ]:
        pdf.table_row(r, w3)

    pdf.body(
        "Взгляд автора: нефть — стратегический ресурс в игре США vs Китай. "
        "Краткосрочные «мирные вбросы» не отменяют долгосрочный рост."
    )

    pdf.add_page()
    pdf.section_title("3. Акции — точки входа")

    pdf.sub_title("Corwave (CRWV)")
    pdf.code_block(
        "     текущая цена\n"
        "        |\n"
        "78,40$ --┴--  <- сквиз = scalp-long (высокий риск)"
    )
    pdf.bullet("78,40$ — высокорисковый scalp-лонг при сквизе к уровню.")

    pdf.sub_title("SanDisk (SNDK)")
    pdf.code_block(
        "1 330–1 300$  <- поддержка | scalp-long, КОРОТКИЙ стоп\n"
        "        |\n"
        "        v  (пробой и закреп ниже)\n"
        "1 100–1 000$  <- уверенный long на норм. объём"
    )
    w4 = [38, 38, 30, 74]
    pdf.table_header(["Зона", "Сделка", "Объём", "Стоп"], w4)
    for r in [
        ("1 330–1 300$", "Scalp long", "Малый", "Короткий, обязательно"),
        ("1 100–1 000$", "Long", "Нормальный", "После пробоя поддержки"),
    ]:
        pdf.table_row(r, w4)

    pdf.sub_title("LITE — отработано")
    pdf.bullet("Вход ~777$ (погрешность 0,5–1%) — сработал, отскок за 2 дня.")
    pdf.bullet("Урок: не «котлетить» в крипте из FOMO, когда акции дают движение быстрее.")

    pdf.sub_title("Intel / Micron — логика без уровней")
    pdf.bullet("Intel — производство в США (Аризона).")
    pdf.bullet("Micron — единственный US-производитель памяти; выигрывает vs Samsung/SK Hynix.")
    pdf.bullet("Трамп публично хвалит → прикрытие от обвинений в инсайде.")

    pdf.section_title("4. Корреляция: крипта ↔ сектор памяти")
    pdf.code_block(
        "Крипта растёт  -->  MU, WDC, SNDK падают\n"
        "Крипта падает  -->  MU, WDC, SNDK отскакивают"
    )
    pdf.body(
        "Идея: аллокация и в крипте, и в секторе памяти как противовес. "
        "Пока внимание на AI — от крипты «сверхъестественного» ждать не стоит."
    )

    pdf.section_title("5. Сводная таблица точек входа")
    w5 = [22, 30, 16, 16, 96]
    pdf.table_header(["Актив", "Уровень", "Напр.", "Риск", "Условие"], w5)
    entries = [
        ("BTC", "76 250", "Long", "Сред.+", "Откат после 79.8–80.25; hawkish Уорш"),
        ("HYPE", "~76 250 BTC", "Long", "Высок.", "Вместе с BTC"),
        ("PUMP", "~76 250 BTC", "Long", "Высок.", "Вместе с BTC"),
        ("ZEC", "В моменте", "Long", "Высок.", "При падении BTC"),
        ("Brent", "Текущая", "Long 1–2x", "Сред.", "Цель 98–102"),
        ("CL", "69,2 / 66,2", "Long", "Сред.", "Откат перед выборами"),
        ("Corwave", "78,40", "Scalp L", "Высок.", "Сквиз к уровню"),
        ("SanDisk", "1330–1300", "Scalp L", "Высок.", "Короткий стоп"),
        ("SanDisk", "1100–1000", "Long", "Сред.", "После пробоя"),
        ("LITE", "777", "Long", "—", "Уже отработано"),
    ]
    for r in entries:
        pdf.table_row(r, w5)

    pdf.section_title("6. Триггеры на сегодня")
    pdf.bullet("17:00 Уорш (Jackson Hole): hawkish → BTC к 76 250.")
    pdf.bullet("Пошлины на чипы: следить за INTC, MU.")
    pdf.bullet("Нефть / Иран: эскалация → Brent к 98–102.")
    pdf.bullet("Не открывать эмоциональные сделки — «котлетить» из FOMO не советуется.")

    pdf.ln(6)
    pdf.set_font("DejaVu", "", 8)
    pdf.set_text_color(120, 120, 120)
    pdf.multi_cell(
        usable,
        4,
        "Дисклеймер: материал — структурированная выжимка обзора с YouTube. "
        "Не является инвестиционной рекомендацией. Торговля сопряжена с риском.",
    )

    pdf.output(str(OUTPUT))
    print(f"Created: {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build_pdf()
