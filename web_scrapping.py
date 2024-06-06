import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_Name = []
Prices = []
Description = []
Reviews = []

def element(price_string):
    return price_string.replace("").replace(",", "").strip()


for i in range(2,12):
    url = ("https://www.flipkart.com/search?q=mobiles+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_19_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+50000%7CMobiles&requestId=6bd1c012-9a98-4d0e-a6ed-3a0c3cb104ae&as-searchtext=mobiles+under+50000&page="+str(i))

  

    try:
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        box = soup.find("div", class_="DOjaWF gdgoEp")
                
        if box is not None:
            # Product name
            names = box.find_all("div", class_ = "KzDlHZ")
            for element in names:
                # name = i.text
                Product_Name.append(element.get_text(strip=True))

            # print(Product_Name)

            # Product price
            prices = box.find_all("div",class_ = "Nx9bqj _4b5DiR")
            
            for element in prices:
                # name = i.text
                Prices.append(element.get_text(strip=True))
            
           
                    
            # print(Prices)

            # Description
            desc = box.find_all("ul", class_= "G4BRas")

            for element in desc:
                # name = i.text
                Description.append(element.get_text(strip=True))
                    
            # print(Description)
                    
                    # reviews
            
            reviews = box.find_all("div",class_ = "XQDdHH")
            for element in reviews:
                # name = i.text
                Reviews.append(element.get_text(strip=True))
        
        # print(Reviews)
        else:
            print("The container element was not found on the page")
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
print("Product_Name", (Product_Name))
print("Prices:", (Prices))
print("Description:", (Description))
print("Reviews:", (Reviews))
    
    
min_length = min(len(Product_Name), len(Prices), len(Description), len(Reviews))

Product_Name = Product_Name[:min_length]
Prices = Prices[:min_length]
Description = Description[:min_length]
Reviews = Reviews[:min_length]
    
df = pd.DataFrame({
    "Product Name":Product_Name,
    "Price ":Prices, 
    "Descriptions":Description, "Review":Reviews})

df.to_csv("output.csv", index = False)
print("DataFrame created and saved successfully")

    
