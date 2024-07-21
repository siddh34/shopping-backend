#include <iostream>
#include "datamodel.h"
#include <vector>
#include <limits>
using namespace std;

vector<Product> products = {
    Product(2, "Banana", 50),
    Product(1, "Apple", 100),
    Product(3, "Orange", 80),
    Product(4, "Grapes", 120),
    Product(5, "Pineapple", 150)};

Product *chooseProduct(vector<Product> &products)
{
    cout << "Choose a product:" << endl;
    for (int i = 0; i < products.size(); i++)
    {
        cout << i + 1 << ". " << products[i].getDisplayName() << endl;
    }
    int choice;
    cin >> choice;
    if (choice < 1 || choice > products.size())
    {
        cout << "Invalid choice. Please select a valid product." << endl;
        return nullptr; // Return nullptr to indicate an invalid choice
    }

    return &products[choice - 1];
}

int main()
{
    char action;
    Cart cart;
    do
    {
        cout << "Choose an action:" << endl;
        cout << "1. View products" << endl;
        cout << "2. Add products to cart" << endl;
        cout << "3. Exit" << endl;
        cout << "4. Remove from cart" << endl;
        cin >> action;
        if (cin.fail())
        {
            cin.clear();                                              // Clear error flags
            cin.ignore(std::numeric_limits<streamsize>::max(), '\n'); // Discard bad input
            continue;                                                 // Skip to the next iteration
        }
        switch (action)
        {
        case '1':
            for (Product p : products)
            {
                cout << p.getDisplayName() << endl;
            }
            break;
        case '2':
        {
            Product *p = chooseProduct(products);
            if (p == nullptr)
            {
                break;
            }
            int quantity;
            cout << "Enter quantity:" << endl;
            if (!(cin >> quantity))
            {
                cin.clear();                                         // Clear error flags
                cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard bad input
                cout << "Invalid quantity." << endl;
                break;
            }
            cout << "Adding to cart: " << p->getName() << " x " << quantity << " for " << p->getPrice() * quantity << endl;
            cart.addItem(*p, quantity);
            break;
        }
        case '4':
        {
            cart.showCart();
            bool flag = false;
            cout << "Enter the product id to remove from cart: ";
            int id;
            if (!(cin >> id))
            {
                cin.clear();                                         // Clear error flags
                cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard bad input
                cout << "Invalid ID." << endl;
                break;
            }
            for (Product pr : products)
            {
                if (pr.getId() == id)
                {
                    flag = true;
                    cart.removeItem(pr);
                    break;
                }
            }
            if (!flag)
            {
                cout << "Product not found in cart." << endl;
            }
            break;
        }
        default:
            break;
        }
    } while (action != '3');

    return 0;
}