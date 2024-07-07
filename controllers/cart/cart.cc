#include "cart.h"

void Cart::addItem(const HttpRequestPtr& req, std::function<void (const HttpResponsePtr &)>&& callback) const {
	// Your logic to add an item to the cart
	auto resp = HttpResponse::newHttpResponse();
	resp->setBody("Item added to cart");
	callback(resp);
}