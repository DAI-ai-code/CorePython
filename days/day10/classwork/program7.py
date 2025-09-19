

try:
    f = open("text.csv",'w')
    f.write("Date,Patient,Procedure,Amount,Insurance_Covered\n")
    f.write("2024-01-15,John Smith,Dental Checkup,150,Yes\n")
    f.write("2024-01-20,Jane Doe,Eye Exam,85,Yes\n")
    f.write("2024-02-03,Robert Johnson,Physical Therapy,200,No\n")
    f.write("2024-02-10,Emily Wilson,Vaccination,120,Yes\n")
    f.write("2024-02-18,Mike Brown,Blood Test,95,Yes")
    f.close()

    f1 = open("text.csv","r")
    data = f1.readlines()
    l = [i for i in range(len(data[0].split(',')))]

    for i in l:
        print(data[0].split(',')[i], end='\t\t\t')
    print('\b')

    for i in range(1,len(data)):
        for j in l:
            print(data[i].split(',')[j], end='\t\t\t')
        print('\b')


except:
    print("e")
finally:
    f.close()


"""
Deepseek code :

try:
    f = open("text.csv", 'w')
    f.write("Date,Patient,Procedure,Amount,Insurance_Covered\n")
    f.write("2024-01-15,John Smith,Dental Checkup,150,Yes\n")
    f.write("2024-01-20,Jane Doe,Eye Exam,85,Yes\n")
    f.write("2024-02-03,Robert Johnson,Physical Therapy,200,No\n")
    f.write("2024-02-10,Emily Wilson,Vaccination,120,Yes\n")
    f.write("2024-02-18,Mike Brown,Blood Test,95,Yes")
    f.close()

    f1 = open("text.csv", "r")
    data = f1.readlines()

    # Get column count from header
    columns = data[0].strip().split(',')

    # Print header with proper formatting
    for col in columns:
        print(f"{col:<20}", end='')  # Left-aligned, 20 characters wide
    print()

    # Print separator line
    print("-" * (20 * len(columns)))

    # Print data rows
    for i in range(1, len(data)):
        row_data = data[i].strip().split(',')
        for item in row_data:
            print(f"{item:<20}", end='')  # Left-aligned, 20 characters wide
        print()

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'f1' in locals():
        f1.close()


"""