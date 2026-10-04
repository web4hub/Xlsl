#pragma once
#include <algorithm>
#include <cmath>
#include <cstddef>
#include <limits>
#include <stdexcept>
#include <vector>

namespace auraxlsl::survival {

struct Record {
    double time{};
    int status{};
    int group{};
};

struct LogRankResult {
    double observed_group1{};
    double expected_group1{};
    double variance{};
    double chi_square{};
    double z{};
    double p_value{};
};

inline LogRankResult log_rank_test(std::vector<Record> records) {
    if (records.empty()) throw std::invalid_argument("log-rank requires records");
    for (const auto& r : records) {
        if (!std::isfinite(r.time) || r.time < 0.0)
            throw std::invalid_argument("time must be finite and non-negative");
        if (r.status != 0 && r.status != 1)
            throw std::invalid_argument("status must be 0 or 1");
        if (r.group != 1 && r.group != 2)
            throw std::invalid_argument("group must be 1 or 2");
    }

    std::sort(records.begin(), records.end(), [](const Record& a, const Record& b) {
        if (a.time != b.time) return a.time < b.time;
        return a.status > b.status;
    });

    double O1 = 0.0, E1 = 0.0, V = 0.0;
    std::size_t i = 0;

    while (i < records.size()) {
        const double t = records[i].time;
        std::size_t j = i;
        while (j < records.size() && records[j].time == t) ++j;

        double N1 = 0.0, N2 = 0.0, O = 0.0, O1t = 0.0;
        for (const auto& r : records) {
            if (r.time >= t) {
                if (r.group == 1) ++N1;
                else ++N2;
            }
        }
        for (std::size_t k = i; k < j; ++k) {
            if (records[k].status == 1) {
                ++O;
                if (records[k].group == 1) ++O1t;
            }
        }

        const double N = N1 + N2;
        if (O > 0.0) {
            O1 += O1t;
            if (N > 1.0) {
                E1 += N1 * O / N;
                V += (N1 * N2 * O * (N - O)) / (N * N * (N - 1.0));
            }
        }
        i = j;
    }

    LogRankResult out;
    out.observed_group1 = O1;
    out.expected_group1 = E1;
    out.variance = V;

    if (V > 0.0) {
        out.z = (O1 - E1) / std::sqrt(V);
        out.chi_square = out.z * out.z;
        out.p_value = std::erfc(std::abs(out.z) / std::sqrt(2.0));
    } else {
        out.z = std::numeric_limits<double>::quiet_NaN();
        out.chi_square = 0.0;
        out.p_value = 1.0;
    }
    return out;
}

}
