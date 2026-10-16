
import tkinter as tk

# ألوان التطبيق
GREEN = "#123F35"
LIGHT_GREEN = "#1C5949"
GOLD = "#E8C878"
CREAM = "#F7F4EA"
WHITE = "#FFFFFF"

# الأذكار
AZKAR = {
    "أذكار الصباح": [
        ("أصبحنا وأصبح الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير.", 1),
        ("سبحان الله وبحمده", 100),
        ("أستغفر الله وأتوب إليه", 100),
    ],
    "أذكار المساء": [
        ("أمسينا وأمسى الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له، له الملك وله الحمد وهو على كل شيء قدير.", 1),
        ("سبحان الله وبحمده", 100),
        ("أستغفر الله وأتوب إليه", 100),
    ],
    "أذكار النوم": [
        ("باسمك اللهم أموت وأحيا", 1),
        ("سبحان الله", 33),
        ("الحمد لله", 33),
        ("الله أكبر", 34),
    ],
}


class HisnMuslim:
    def __init__(self, root):
        self.root = root
        self.root.title("حصن المسلم")
        self.root.geometry("540x680")
        self.root.minsize(320, 500)
        self.root.configure(bg=CREAM)

        self.count = 0
        self.tasbeeh_count = 0
        self.items = []
        self.index = 0
        self.current_name = ""

        # عنوان التطبيق
        self.header = tk.Label(
            root,
            text="حِصْنُ المُسْلِم",
            font=("Arial", 26, "bold"),
            bg=GREEN,
            fg=GOLD,
            pady=20
        )
        self.header.pack(fill="x")

        self.content = tk.Frame(root, bg=CREAM)
        self.content.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=18
        )

        self.home()

    def clear(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def make_button(self, text, command):
        return tk.Button(
            self.content,
            text=text,
            command=command,
            font=("Arial", 15, "bold"),
            bg=LIGHT_GREEN,
            fg=WHITE,
            activebackground=GOLD,
            activeforeground=GREEN,
            relief="flat",
            cursor="hand2",
            wraplength=420,
            padx=10,
            pady=12
        )

    def home(self):
        self.clear()

        tk.Label(
            self.content,
            text="أذكارك اليومية وطمأنينة قلبك",
            font=("Arial", 16),
            bg=CREAM,
            fg=GREEN,
            wraplength=450
        ).pack(pady=15)

        for name in AZKAR:
            self.make_button(
                name,
                lambda n=name: self.open_azkar(n)
            ).pack(fill="x", pady=7)

        self.make_button(
            "السبحة الإلكترونية",
            self.tasbeeh
        ).pack(fill="x", pady=7)

        tk.Label(
            self.content,
            text="نسأل الله أن ينفعنا وإياكم",
            font=("Arial", 11),
            bg=CREAM,
            fg=GREEN
        ).pack(side="bottom", pady=10)

    def open_azkar(self, name):
        self.current_name = name
        self.items = AZKAR[name]
        self.index = 0
        self.count = 0
        self.show_zikr()

    def show_zikr(self):
        self.clear()

        if self.index >= len(self.items):
            tk.Label(
                self.content,
                text="أحسنت! أتممت هذه الأذكار",
                font=("Arial", 20, "bold"),
                bg=CREAM,
                fg=GREEN,
                wraplength=440
            ).pack(expand=True)

            self.make_button(
                "العودة للرئيسية",
                self.home
            ).pack(fill="x", pady=10)
            return

        zikr, target = self.items[self.index]

        tk.Label(
            self.content,
            text=self.current_name,
            font=("Arial", 19, "bold"),
            bg=CREAM,
            fg=GREEN
        ).pack(pady=10)

        tk.Label(
            self.content,
            text=zikr,
            font=("Arial", 20),
            bg=CREAM,
            fg=GREEN,
            wraplength=450,
            justify="center"
        ).pack(fill="both", expand=True, pady=20)

        tk.Label(
            self.content,
            text=f"التكرار: {self.count} / {target}",
            font=("Arial", 16, "bold"),
            bg=CREAM,
            fg=LIGHT_GREEN
        ).pack(pady=10)

        def repeat():
            self.count += 1

            if self.count >= target:
                self.index += 1
                self.count = 0

            self.show_zikr()

        self.make_button(
            "✓ تم الذكر",
            repeat
        ).pack(fill="x", pady=7)

        self.make_button(
            "العودة للرئيسية",
            self.home
        ).pack(fill="x", pady=7)

    def tasbeeh(self):
        self.clear()

        tk.Label(
            self.content,
            text="السبحة الإلكترونية",
            font=("Arial", 21, "bold"),
            bg=CREAM,
            fg=GREEN
        ).pack(pady=15)

        counter = tk.Label(
            self.content,
            text=str(self.tasbeeh_count),
            font=("Arial", 48, "bold"),
            bg=CREAM,
            fg=GREEN
        )
        counter.pack(pady=25)

        tk.Label(
            self.content,
            text="سبحان الله",
            font=("Arial", 22),
            bg=CREAM,
            fg=LIGHT_GREEN
        ).pack(pady=10)

        def increment():
            self.tasbeeh_count += 1
            counter.config(text=str(self.tasbeeh_count))

        def reset():
            self.tasbeeh_count = 0
            counter.config(text="0")

        self.make_button(
            "تسبيح +1",
            increment
        ).pack(fill="x", pady=7)

        self.make_button(
            "تصفير العداد",
            reset
        ).pack(fill="x", pady=7)

        self.make_button(
            "العودة للرئيسية",
            self.home
        ).pack(fill="x", pady=7)


if __name__ == "__main__":
    root = tk.Tk()
    app = HisnMuslim(root)
    root.mainloop()
