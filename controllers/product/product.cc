#include "product.h"

void Product::getProduct(const HttpRequestPtr &req, std::function<void(const HttpResponsePtr &)> &&callback, int productId) const
{
    // Your logic to fetch and return a product
    auto resp = HttpResponse::newHttpResponse();
    resp->setBody("Product details for product " + std::to_string(productId));
    callback(resp);
}