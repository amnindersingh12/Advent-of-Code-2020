a = open("day1_test_case.txt", "r").read().splitlines()
# a= [1721,979,366,299,675,1456]
a = list(map(int,a))
n = len(a)
# print((a))
for i in range(n):
    for j in range(i+1,n):
        # print(a[i],a[j])
        if a[i]+a[j] == 2020:
            print("Numbers are : ", a[i],a[j])
            print("First :",a[i]*a[j])
        for k in range(j+1,n):
            if a[i]+a[j]+a[k] == 2020:
                print("Numbers are : ", a[i],a[j],a[k])
                print("second :",a[i]*a[j]*a[k])

        