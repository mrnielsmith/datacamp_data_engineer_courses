import my_package

# instantiance object
print('\nCreate object and show:' + '-'*50)
our_data_shell = my_package.DataShell('test.csv')
our_data_shell.show_shell()

# test changing column name ('a' did not work when reading from csv, so i used c and then a for a change test)
print('\nRename column test:' + '-'*50)
our_data_shell.array = our_data_shell.rename_column('c','a')
our_data_shell.array = our_data_shell.rename_column('a','C')
our_data_shell.show_shell()

# test summary
print('\nSummary test for column 0 and 1:' + '-'*50)
print(our_data_shell.five_figure_summary(0))
print(our_data_shell.five_figure_summary(1))

# child object
print('\nChild object and stdev test:' + '-'*50)
st_dev_shell = my_package.StDevShell('test.csv')
print(st_dev_shell.get_stdev(1))
