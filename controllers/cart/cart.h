#pragma once
#include <drogon/HttpController.h>
using namespace drogon;

class Cart : public drogon::HttpController<Cart>
{
public:
    METHOD_LIST_BEGIN
    // Add methods definitions here; METHOD_ADD(method, path, HttpMethod);
    METHOD_ADD(Cart::addItem, "/cart/add", Post); // Example endpoint
    METHOD_LIST_END

    // Method implementation
    void addItem(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback) const;
};