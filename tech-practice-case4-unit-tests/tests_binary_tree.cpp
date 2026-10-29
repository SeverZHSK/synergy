#include <gtest/gtest.h>

#include "binary_tree.hpp"

TEST(BinaryTreeTest, EmptyInitially) {
    BinaryTree t;
    EXPECT_TRUE(t.empty());
}

TEST(BinaryTreeTest, SearchMissingReturnsFalse) {
    BinaryTree t;
    EXPECT_FALSE(t.search(42));
}

TEST(BinaryTreeTest, PushThenSearchReturnsTrue) {
    BinaryTree t;
    t.push(10);
    t.push(5);
    t.push(15);

    EXPECT_TRUE(t.search(10));
    EXPECT_TRUE(t.search(5));
    EXPECT_TRUE(t.search(15));
    EXPECT_FALSE(t.search(7));
}

TEST(BinaryTreeTest, PopLeafNode) {
    BinaryTree t;
    for (int v : {10, 5, 15}) {
        t.push(v);
    }
    t.pop(5);
    EXPECT_FALSE(t.search(5));
    EXPECT_TRUE(t.search(10));
    EXPECT_TRUE(t.search(15));
}

TEST(BinaryTreeTest, PopNodeWithOneChild) {
    BinaryTree t;
    for (int v : {10, 5, 15, 3}) {
        t.push(v);
    }
    t.pop(5);
    EXPECT_FALSE(t.search(5));
    EXPECT_TRUE(t.search(3));
    EXPECT_TRUE(t.search(10));
}

TEST(BinaryTreeTest, PopNodeWithTwoChildren) {
    BinaryTree t;
    for (int v : {10, 5, 15, 3, 7, 12, 20}) {
        t.push(v);
    }
    t.pop(5);
    EXPECT_FALSE(t.search(5));
    for (int v : {10, 15, 3, 7, 12, 20}) {
        EXPECT_TRUE(t.search(v));
    }
}

TEST(BinaryTreeTest, PopRootNode) {
    BinaryTree t;
    for (int v : {10, 5, 15}) {
        t.push(v);
    }
    t.pop(10);
    EXPECT_FALSE(t.search(10));
    EXPECT_TRUE(t.search(5));
    EXPECT_TRUE(t.search(15));
}

TEST(BinaryTreeTest, PushDuplicateIsIgnored) {
    BinaryTree t;
    t.push(10);
    t.push(10);
    t.pop(10);
    EXPECT_FALSE(t.search(10));
}
