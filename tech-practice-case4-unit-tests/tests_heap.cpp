#include <gtest/gtest.h>

#include <vector>

#include "heap.hpp"

TEST(HeapTest, EmptyInitially) {
    Heap h;
    EXPECT_TRUE(h.empty());
    EXPECT_EQ(h.size(), 0u);
}

TEST(HeapTest, PushIncreasesSize) {
    Heap h;
    h.push(5);
    h.push(3);
    EXPECT_EQ(h.size(), 2u);
}

TEST(HeapTest, TopIsMaximum) {
    Heap h;
    h.push(5);
    h.push(15);
    h.push(3);
    h.push(9);
    EXPECT_EQ(h.top(), 15);
}

TEST(HeapTest, PopRemovesInDescendingOrder) {
    Heap h;
    for (int v : {4, 10, 1, 7, 15, 2}) {
        h.push(v);
    }

    std::vector<int> popped;
    while (!h.empty()) {
        popped.push_back(h.top());
        h.pop();
    }

    ASSERT_EQ(popped.size(), 6u);
    for (size_t i = 1; i < popped.size(); ++i) {
        EXPECT_GE(popped[i - 1], popped[i]);
    }
    EXPECT_EQ(popped.front(), 15);
    EXPECT_EQ(popped.back(), 1);
}

TEST(HeapTest, PopOnEmptyThrows) {
    Heap h;
    EXPECT_THROW(h.pop(), std::out_of_range);
}

TEST(HeapTest, TopOnEmptyThrows) {
    Heap h;
    EXPECT_THROW(h.top(), std::out_of_range);
}
