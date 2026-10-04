#include <cassert>
#include <cmath>
#include <vector>
#include "../engine/include/auraxlsl/survival/log_rank.hpp"

int main() {
    using auraxlsl::survival::Record;
    using auraxlsl::survival::log_rank_test;

    const std::vector<Record> data{
        {1,1,1}, {2,1,1}, {3,0,1}, {4,1,1},
        {1,0,2}, {2,1,2}, {3,1,2}, {5,0,2}
    };

    const auto r = log_rank_test(data);
    assert(std::isfinite(r.z));
    assert(r.variance > 0.0);
    assert(r.chi_square >= 0.0);
    assert(r.p_value >= 0.0 && r.p_value <= 1.0);
    assert(std::abs(r.chi_square - r.z * r.z) < 1e-12);
    return 0;
}
