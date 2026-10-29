#pragma once

#include <cstddef>
#include <stdexcept>
#include <utility>
#include <vector>

class Heap {
public:
    void push(int value) {
        data_.push_back(value);
        siftUp(data_.size() - 1);
    }

    void pop() {
        if (data_.empty()) {
            throw std::out_of_range("pop from empty heap");
        }
        data_.front() = data_.back();
        data_.pop_back();
        if (!data_.empty()) {
            siftDown(0);
        }
    }

    int top() const {
        if (data_.empty()) {
            throw std::out_of_range("top of empty heap");
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
    std::vector<int> data_;

    void siftUp(std::size_t index) {
        while (index > 0) {
            std::size_t parent = (index - 1) / 2;
            if (data_[parent] >= data_[index]) {
                break;
            }
            std::swap(data_[parent], data_[index]);
            index = parent;
        }
    }

    void siftDown(std::size_t index) {
        std::size_t size = data_.size();
        while (true) {
            std::size_t left = 2 * index + 1;
            std::size_t right = 2 * index + 2;
            std::size_t largest = index;

            if (left < size && data_[left] > data_[largest]) {
                largest = left;
            }
            if (right < size && data_[right] > data_[largest]) {
                largest = right;
            }
            if (largest == index) {
                break;
            }
            std::swap(data_[index], data_[largest]);
            index = largest;
        }
    }
};
