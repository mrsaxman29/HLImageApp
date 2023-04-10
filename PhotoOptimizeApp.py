import shopify
import urllib
from PIL import Image

## Admin API access token


shopify.ShopifyResource.set_site(shop_url)
shopify.Session.setup(api_key=API_KEY, secret=ONCE)
shop = shopify.Shop.current

def optomize_photo(img_name, save_name):
    pic = Image.open(img_name)
    new_pic = pic.convert('RGB')
    new_pic.save(save_name,
                 "WEBP",
                 optimize=True,
                 quality=40)

def download_all_images():
    counter = 0

    user_input = int(input('ENTER COLLECTION ID NUMBER: '))
    collection_to_search = shopify.Product.find(collection_id=user_input)

    for product in collection_to_search:
        print(f'Product ID: {product.id}')
        print(f'product title:{product.title}')
        product_name = product.title
        product_name = product_name.replace(" ","_")
        print(product_name)


        for image in product.images:
            print(image.src)
            img_url = image.src
            img_id = image.id
            img_id = str(img_id)
            img_id += '.jpg'
            new_name = product_name + str(counter) +'.jpg'
            print(new_name, img_url)
            urllib.request.urlretrieve(img_url, img_id)
            optomize_photo(img_id, new_name)

            counter +=1

        counter = 0


test_list = shopify.Product.find(collection_id=281277235257)
eco_list = shopify.Product.find(collection_id=281267699769)     #ECO CRYSTAL
market_list = shopify.Product.find(collection_id=275689570361)

download_all_images()





################ VARIOUS FUNCTIONS / METHODS FOR ACCESSING API BELOW  #################

####  GETS PRODUCT OBJECT FROM API
product = shopify.Product.find(6812006121529)
print(product.attributes)
print(f'LIST OF IMAGES: {product.images}')

## FINDS URL OF PRODUCT IMAGE
print(product.image.src)

### Find Inventory Quantity
print(product.variants[0].inventory_quantity)

### FIND COLLECTION

def find_collection():
    products = shopify.Product.find(collection_id=275689701433)     #Oven to Table
    print(len(products))
    print(f"LIST OF PRODUCTS {products}")
    print(f'LIST OF PRODUCT IMAGES {products[0].images}')

    return products

## for product in collection - This Dowloads Product Image To CWD

## make so all photos not just featured photo downloads

def download_images():

    items = find_collection()

    for x in items:
        print(x.image.src)
        print(x.image.id)
        img_url = x.image.src
        img_id = x.image.id
        img_id = str(img_id)
        img_id += '.jpg'
        print(img_id)
        urllib.request.urlretrieve(img_url, img_id)

        print('Images Downloaded')

#download_images()

###### ABOVE IS STABLE

"""
COMPLETED:

Kitchen Linens
Market
Kitchen Tools (not harvest serving set, Rustic Walnut Utensil, hand forged cheese knife
bone scoop)
Eco Crystal (active only)
Coupes (and berlyn petit goblet)
Serveware



TO DO:

Make Conversion go to WEBP not JPEG
Make Function to do just 1 product not a collection
Make Alt Image Text = to new image name

Add Function to upload new photos and delete old ones



"""
