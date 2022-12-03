import subprocess
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="VIT for OCT2017",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--start", type=int, help=f"Fist HPC number", default=11)
    parser.add_argument("-e", "--end", type=int, help=f"Last HPC number", default=50)
    args = parser.parse_args()
    config = vars(args)
    return config
            

args = parse_args()
start =  args["start"] or args["i"]
end = args["end"] or args["e"] 

# hpc start from .11
start = start if start >= 11 else 11


# best_hpc = []
best_hpc = ""
best_avail = 0


for i in range(start,end):
    try:
        answer = subprocess.check_output(['./check_cuda.sh', f"10.127.30.{i}"])
        answer = str(answer, encoding='utf-8')
        answer = answer.split("\n")[-3:]
        availability = 1-int(answer[0])/int(answer[1])
        if int(answer[1])>24000:
            print(f"10.127.30.{i}: {float('{:.2f}'.format(availability))*100}% ")

            # find best
            if availability>best_avail:
                # best_hpc.append(f"10.127.30.{i}: {float('{:.2f}'.format(availability))*100}% , Total:  {answer[1]}")
                best_hpc = f"10.127.30.{i}: {float('{:.2f}'.format(availability))*100}%"
                best_avail = availability

    except:
       print("Unreachable")


print('')
print('')
print('')
print("Best HPC:")
print('')
print(best_hpc)

# for i in best_hpc:
#     print(i)