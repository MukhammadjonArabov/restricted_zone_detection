# Restricted Zone Detection

**Qisqacha:** Videodagi odamlarni aniqlash uchun YOLO dan foydalanadigan va agar biror kishi cheklangan zonaga kirsa, signal beruvchi oddiy tizim.

## Xususiyatlari
- Videoning birinchi kadrida bir yoki bir nechta ko'pburchakli cheklangan zonalarni chizish (sichqoncha bilan chizish).
- Zonalar `restricted_zone.json` ga saqlangan.
- Shaxsni aniqlash uchun YOLO (Ultralytics) dan foydalanadi.
- Chegara qutilarini, markazlarni, zonalarni vizualizatsiya qiladi va odam zona ichida bo'lganida qizil rangda `ALARM!` ni ko'rsatadi.
- Odamlar zonani tark etgandan 3 soniya o'tgach, signal avtomatik ravishda o'chiriladi.

## Talablar
- Python 3.11+
- Faqat protsessorda foydalanish qo'llab-quvvatlanadi
- Loyiha `ultralytics` paketidan (YOLOv8) foydalanadi. U birinchi ishga tushirishda og'irliklarni avtomatik ravishda yuklab oladi. Agar siz og'irliklarni yuklab ololmasangiz, afzal ko'rgan YOLO og'irliklaringizdan foydalaning va `detector.py` ni yangilang.

O'rnatish
```bash
git clone https://github.com/MukhammadjonArabov/restricted_zone_detection.git
py -m venv venv
\.venv\Scripts\activate
pip install -r requirements.txt
```
- Chegarani chizish uchun. Sichqonchani chap tugmasi bosib nuqtalarni belgilab chegara chiziladi eng kamida 3 ta nuqta
- c tugmani bosib chizgan zona saqlanadi
- r tugma esa chizgan chegarani o'chiradi kayin yana qaytadan chizish mumkun
- esc tugma dasturni to'xtatadi
- videos/test.mp4 Loyhada videos fayili va uni ichida test.mp4 nomliy video bo'lsin yoki boshqacha bo'lsa buyruq shunga qarab o'zgaratdi
```bash
python main.py -v videos/test.mp4 --draw
```
- c ni bosib chizgan zonani saqlagandan keyin quydagi buyruqni ishga tushurasiz
```bash
python main.py -v videos/test.mp4
```
## Loyhani bajarganda quydagi manbalardan foydalandim
- https://github.com/ultralytics/ultralytics?tab=readme-ov-file
- https://docs.opencv.org/4.x/
- https://www.geeksforgeeks.org/python/opencv-python-tutorial/
- https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html
- https://www.geeksforgeeks.org/computer-vision/opencv-projects-ideas-for-beginners/

## OpenCV va YOLO ni o'rganib chiqib, bu loyhani bajarishdan oldin quydagi kichik loyhalarni qildim
- https://github.com/MukhammadjonArabov/OpenCV-projects
- https://github.com/MukhammadjonArabov/OpenCV-Django

## Qiyilchilik
- Loyhani qilishda chizilgan zonaga odam kesib o'tganini anilab olishda qiyinchilik bo'ldi.
- Bu muammoni odamni aniqlab olib odamni markazidan nuqta oldim va shu nuqtani chizilgan chegaraga kirish yoki kirmasligini tekshirdim
