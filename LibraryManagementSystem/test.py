

class Library:
    def __init__(self, filename="books.txt"):
        # Dosya adı tanımlanıyor ve "a+" modunda açılıyor.
        self.filename = filename
        self.file = open(self.filename, "a+", encoding='utf-8')

    def __del__(self):
        # Dosya kapatılıyor.
        self.file.close()

    def list_books(self):
        # Dosyanın başına gidiliyor.
        self.file.seek(0)
        # Dosyanın içeriği okunuyor.
        books = self.file.read().splitlines()
        # Kitaplar listeleniyor.
        for book in books:
            title, author, year, pages = book.split(', ')
            print(f"Kitap Adı: {title}, Yazar: {author}")

    def add_book(self):
        title = input("Kitap adını giriniz: ")
        author = input("Yazarın adını giriniz: ")
        year = input("İlk yayın yılını giriniz: ")
        pages = input("Sayfa sayısını giriniz: ")
        # Kitap bilgileri dosyaya ekleniyor.
        self.file.write(f"{title}, {author}, {year}, {pages}\n")
        self.file.flush()

    def remove_book(self):
        title_to_remove = input("Kaldırılacak kitabın adını giriniz: ")
        self.file.seek(0)
        # Dosyanın içeriği okunuyor ve bir listeye ekleniyor.
        books = self.file.read().splitlines()
        # Silinecek kitabın bulunması ve kaldırılması.
        books = [book for book in books if not book.startswith(title_to_remove)]
        # Dosyanın içeriğini temizleme ve yeni listeyi yazma.
        self.file.seek(0)
        self.file.truncate()
        for book in books:
            self.file.write(f"{book}\n")
        self.file.flush()

# Library sınıfı ile bir nesne oluşturuluyor.
lib = Library()

# Kullanıcı menüsü
while True:
    print("*** MENÜ ***\n1. Kitapları Listele\n2. Kitap Ekle\n3. Kitap Kaldır\n4. Çıkış")
    choice = input("Seçiminizi yapın (1/2/3/4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")