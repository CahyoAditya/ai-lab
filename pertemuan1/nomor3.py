"""
================================ NOMOR 3 ========================================

    Body Mass Index (BMI) merupakan salah satu cara untuk mengetahui rentang berat
badan ideal Anda dan memprediksi seberapa besar risiko gangguan kesehatan Anda.
Metode ini digunakan untuk menentukan berat badan yang sehat berdasarkan berat dan
tinggi badan. Nilai BMI didapat dari formula berikut :
"""

weight, height = map(float, input().split())
height = height / 100
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Below normal weight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Class I Obesity")
elif bmi < 40:
    print("Class II Obesity")
else:
    print("Class III Obesity")
