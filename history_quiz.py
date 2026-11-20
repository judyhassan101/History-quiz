import random

# list of dictionaries: كل سؤال هو dictionary
questions = [
    {"q": "تمثل العنصر الرئيسي المحرك للأحداث خلال العصور الحديثة ",
     "options": ["1) قيام الثورة الصناعية", "2) حركة الكشوف الجغرافية ", "3) ظهور النهضة الأوروبية"],
     "answer": "3"},
    {"q": "تخطت مظاهر الحضارة نطاق محيط الكرة الأرضية خلال",
     "options": ["1) التاريخ المعاصر", "2) العصور الحديثة", "3) العصور الوسطى"],
     "answer": "1"},
    {"q": "صح أو خطأ : تختلف كتابات المؤرخين عن كتابات الفلاسفة في أنها متوفرة وسهلة الحصول عليها",
     "options": ["1) صح", "2) خطأ"],
     "answer": "2"},
    {"q": " صح او خطأ : يمكن معرفة التقسيم الاداري في مصر الفرعونية من خلال كتابات هيرودوت ",
     "options": ["1) صح", "2) خطأ"],
     "answer": "1"},
]

def ask_question(item):
 # بتعرف هل الاجابة صحيحة او لا ، و تمرر الاجابة الصحيحة
    print("\n" + item["q"])
    for option in item["options"]:
        print(option)
    user_answer = input("اجابتك: ").strip()
    if user_answer == item["answer"]:
        print("صحيحة! ✅")
        return True
    else:
        print("خطأ ❌الاجابة هي  ", item["answer"])
        return False

def main():
    score = 0
    random.shuffle(questions)       #  ترتيب عشوائي للأسألة
    for item in questions:          # loop عشان تعرض كل سؤال
        if ask_question(item):      
            score += 1              # تضيف نقطة لكل سؤال صحيح
    print(f"\nنتيجتك النهائية: {score}/{len(questions)}")
    if score == len(questions):      # لو عدد الأسألة الصحيحة بيساوي عدد الأسألةالمعروضة كلها يبقي ممتاز
        print("ممتاز! 🎉")
    elif score >= len(questions) / 2: # لو عدد الأسألة الصحيحة اكبر من او يساوي نصف الأسألة يبقي جيد جدا
        print("جيد جدًا!")
    else:
        print("أكمل المذاكرة!") # لو اخر شرط و هو انه يكون جاوب اقل من نص الاسألة يبقي اكمل المذاكرة

main()
