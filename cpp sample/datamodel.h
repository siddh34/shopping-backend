#include<iostream>
#include<string>
#include<unordered_map>
using namespace std;

class Item;

class Product {
    int id;
    string name;
    int price;
public:
    Product(int id, string name, int price) {
        this->id = id;
        this->name = name;
        this->price = price;
    }

    string getDisplayName() {
        return name + " (" + to_string(price) + ")";
    }

    string getName() {
        return name;
    }

    int getId() {
        return id;
    }

    int getPrice() {
        return price;
    }

    friend class Item;
};

class Item
{
    Product product;
    int quantity;

public:
    // Default constructor
    Item() : product(0, "", 0), quantity(0) {}

    // Existing constructor
    Item(Product p, int q) : product(p), quantity(q) {}

    Product getProduct()
    {
        return product;
    }

    int getQuantity()
    {
        return quantity;
    }

    int getTotalPrice()
    {
        return product.price * quantity;
    }

    string getItemInfo()
    {
        return product.id + " " + product.name + " x " + to_string(quantity) + " = " + to_string(getTotalPrice());
    }

    friend class Cart;
};

class Cart {
    unordered_map<int, Item> items;
public:
    void addItem(Product p, int quantity) {
        if (items.find(p.getId()) == items.end()) {
            items[p.getId()] = Item(p, quantity);
        } else {
            items[p.getId()] = Item(p, items[p.getId()].getQuantity() + quantity);
        }
    }

    void removeItem(Product p) {
        if(items.empty()) {
            cout << "Cart is empty." << endl;
            return;
        }

        if (items.find(p.getId()) == items.end()) {
            cout << "Product not found in cart." << endl;
            return;
        }

        cout << "Removing from cart: " << p.getName() << " x " << items[p.getId()].getQuantity() << " for " << items[p.getId()].getTotalPrice() << endl;

        items.erase(p.getId());
    }

    void showCart() {
        for (auto& item: items) {
            cout << item.second.getItemInfo() << endl;
        }
    }

    int getTotalPrice() {
        int total = 0;
        for (auto& item: items) {
            total += item.second.getTotalPrice();
        }
        return total;
    }
};