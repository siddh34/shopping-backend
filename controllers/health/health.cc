#include "health.h"

void HealthCheck::check(const drogon::HttpRequestPtr& req, std::function<void (const drogon::HttpResponsePtr &)>&& callback) const {
	auto resp = drogon::HttpResponse::newHttpResponse();
	resp->setStatusCode(drogon::HttpStatusCode::k200OK);
	resp->setBody("Service is up and running");
	callback(resp);
}