#pragma once
#include <drogon/HttpController.h>

class HealthCheck : public drogon::HttpController<HealthCheck> {
public:
	METHOD_LIST_BEGIN
		METHOD_ADD(HealthCheck::hello,"/", drogon::Get, drogon::Post);
		METHOD_ADD(HealthCheck::check, "/healthcheck", drogon::Get, drogon::Post);
	METHOD_LIST_END

	// Method to handle the health check requests.
	void check(const drogon::HttpRequestPtr& req, std::function<void (const drogon::HttpResponsePtr &)>&& callback) const;
	void hello(const drogon::HttpRequestPtr& req, std::function<void (const drogon::HttpResponsePtr &)>&& callback) const;
};