#include <gtest/gtest.h>

#include "queue.hpp"

TEST(QueueTest, EmptyInitially) {
    Queue q;
    EXPECT_TRUE(q.empty());
    EXPECT_EQ(q.size(), 0u);
}

TEST(QueueTest, PushIncreasesSize) {
    Queue q;
    q.push(1);
    q.push(2);
    EXPECT_EQ(q.size(), 2u);
    EXPECT_FALSE(q.empty());
}

TEST(QueueTest, FifoOrder) {
    Queue q;
    q.push(10);
    q.push(20);
    q.push(30);

    EXPECT_EQ(q.front(), 10);
    q.pop();
    EXPECT_EQ(q.front(), 20);
    q.pop();
    EXPECT_EQ(q.front(), 30);
    q.pop();
    EXPECT_TRUE(q.empty());
}

TEST(QueueTest, PopOnEmptyThrows) {
    Queue q;
    EXPECT_THROW(q.pop(), std::out_of_range);
}

TEST(QueueTest, FrontOnEmptyThrows) {
    Queue q;
    EXPECT_THROW(q.front(), std::out_of_range);
}
