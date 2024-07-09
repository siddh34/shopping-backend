#include "health.h"

void HealthCheck::hello(const drogon::HttpRequestPtr& req, std::function<void (const drogon::HttpResponsePtr &)>&& callback) const {
	printf("Adding item to cart\n");
	auto resp = drogon::HttpResponse::newHttpResponse();
	resp->setStatusCode(drogon::HttpStatusCode::k200OK);
	resp->setBody("Hello, World!");
	callback(resp);
}

void HealthCheck::check(const drogon::HttpRequestPtr& req, std::function<void (const drogon::HttpResponsePtr &)>&& callback) const {
	printf("Adding item to cart\n");
	auto resp = drogon::HttpResponse::newHttpResponse();
	resp->setStatusCode(drogon::HttpStatusCode::k200OK);
	resp->setBody("Service is up and running");
	callback(resp);
}