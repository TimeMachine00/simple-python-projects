heights = (input("eneter each subject marks seperated by space").split())
for j in range(0, len(heights)):
    heights[j] = int(heights[j])
print(heights)
total = 0
for i in heights:
    total += i
print(total)
sub =0
for k in heights:
    sub+=1
print(sub)

print("the avg is", round(total/sub))

