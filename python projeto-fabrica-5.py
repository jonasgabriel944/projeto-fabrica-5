import os 
os.system("cls")

print("=== Crescimento Populacional: País A vs País B ===")

pop_a = 80000
pop_b = 200000
taxa_a = 3
taxa_b = 1.5
anos = 0

while True:
    pop_a = pop_a + (pop_a * taxa_a / 100)
    pop_b = pop_b + (pop_b * taxa_b / 100)
    anos += 1

    if pop_a >= pop_b:
        print(f"Após {anos} anos, A alcança/ultrapassa B.")
        print("População final estimada:")
        print(f"- País A: {pop_a} habitantes")
        print(f"- País B: {pop_b} habitantes")