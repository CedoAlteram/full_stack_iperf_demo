import glob, os, subprocess

os.chdir('/Users/Adama/Desktop/perf/iperf_logs')
path = '/Users/Adama/Desktop/perf/iperf_logs'

def getYoungestFile():
    files = sorted(os.listdir(path), key=os.path.getctime)
    newest = files[-1]
    return newest

print getYoungestFile(), "this is the youngest file"
f = open(getYoungestFile(), 'r')
lines = f.readlines()[3:13]
numbers = []
for line in lines:
    print float(line[38:42])
    numbers.append(float(line[38:42]))
f.close()
print numbers
