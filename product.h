#pragma once
#include <drogon/HttpController.h>
using namespace drogon;

class Product : public drogon::HttpController<Product, false>
{
public:
    METHOD_LIST_BEGIN
        METHOD_ADD(Product::getProduct, "/product/{id}", Get); 
    METHOD_LIST_END

    void getProduct(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback, int productId) const;
};