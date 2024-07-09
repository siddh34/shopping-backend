#include <drogon/drogon.h>
#include "cart.h"
#include "product.h"
#include "health.h"
using namespace drogon;

int main() {
    app().registerController(std::make_shared<HealthCheck>());
    app().addListener("0.0.0.0", 5555).setThreadNum(16);
    app().run();
    return 0;
}
