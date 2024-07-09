#include "cart.h"

void Cart::addItem(const HttpRequestPtr& req, std::function<void (const HttpResponsePtr &)>&& callback) const {
	
	auto resp = HttpResponse::newHttpResponse();
	resp->setBody("Item added to cart");
	callback(resp);
}