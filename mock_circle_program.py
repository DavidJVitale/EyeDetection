mock_file_contents='0,1,2\n3,4,5\n6,7,8'

f = open('output.csv','w')
f.write(mock_file_contents)

print('output.csv')
exit(0)