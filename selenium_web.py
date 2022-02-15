from selenium import webdriver

browser = webdriver.Chrome("/home/tejashree/Downloads/chromedriver_linux64/chromedriver")
browser.get("https://demo.guru99.com/test/web-table-element.php")

tbl = browser.find_element_by_xpath("/html/body/div/div[3]/div[1]/table/tbody")
print("tbl: ", tbl.text)

row = browser.find_elements_by_tag_name("tr")
print("Rows present in given webTable is:", len(row))
count = 0
for key in row:
    print("Data from row "+str(count)+" is: ", key.text)
    count += 1
print("Total count for rows : ", count)

header = browser.find_elements_by_tag_name("th")
lis = []
for key in header:
    lis.append(key.text)
print("Header of webTable is as follows: ", lis)
print("Column present in given webTable is:", len(lis))
cols = len(lis)

# for key in range(cols):
#     for keyin in range(len(row)):
#         print(tbl.text[keyin][key])
#     print()

browser.quit()
# =======================================================================