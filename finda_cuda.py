import subprocess

best_hpc = []

for i in range(12,30):
    try:
        answer = subprocess.check_output(['./check_cuda.sh', f"10.127.30.{i}"])
        answer = str(answer, encoding='utf-8')
        answer = answer.split("\n")[-3:]
        available = 1-int(answer[0])/int(answer[1])
        print(f"10.127.30.{i}: {float('{:.2f}'.format(available))*100}% , Total:  {answer[1]}")
    except:
       print("Unreachable")
