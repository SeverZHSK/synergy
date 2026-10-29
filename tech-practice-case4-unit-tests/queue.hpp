#pragma once

#include <cstddef>
#include <deque>
#include <stdexcept>

class Queue {
public:
    void push(int value) {
        data_.push_back(value);
    }

    void pop() {
        if (data_.empty()) {
            throw std::out_of_range("pop from empty queue");
        }
        data_.pop_front();
    }

    int front() const {
        if (data_.empty()) {
            throw std::out_of_range("front of empty queue");
        }
        return data_.front();
    }

    bool empty() const {
        return data_.empty();
    }

    std::size_t size() const {
        return data_.size();
    }

private:
    std::deque<int> data_;
};
