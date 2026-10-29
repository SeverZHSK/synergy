#pragma once

#include <memory>
#include <utility>

class BinaryTree {
public:
    void push(int value) {
        root_ = insert(std::move(root_), value);
    }

    bool search(int value) const {
        Node* node = root_.get();
        while (node != nullptr) {
            if (value == node->value) {
                return true;
            }
            node = value < node->value ? node->left.get() : node->right.get();
        }
        return false;
    }

    void pop(int value) {
        root_ = remove(std::move(root_), value);
    }

    bool empty() const {
        return root_ == nullptr;
    }

private:
    struct Node {
        int value;
        std::unique_ptr<Node> left;
        std::unique_ptr<Node> right;
        explicit Node(int v) : value(v) {}
    };

    std::unique_ptr<Node> root_;

    static std::unique_ptr<Node> insert(std::unique_ptr<Node> node, int value) {
        if (!node) {
            return std::make_unique<Node>(value);
        }
        if (value < node->value) {
            node->left = insert(std::move(node->left), value);
        } else if (value > node->value) {
            node->right = insert(std::move(node->right), value);
        }
        return node;
    }

    static Node* findMin(Node* node) {
        while (node->left) {
            node = node->left.get();
        }
        return node;
    }

    static std::unique_ptr<Node> remove(std::unique_ptr<Node> node, int value) {
        if (!node) {
            return node;
        }
        if (value < node->value) {
            node->left = remove(std::move(node->left), value);
        } else if (value > node->value) {
            node->right = remove(std::move(node->right), value);
        } else {
            if (!node->left) {
                return std::move(node->right);
            }
            if (!node->right) {
                return std::move(node->left);
            }
            Node* successor = findMin(node->right.get());
            node->value = successor->value;
            node->right = remove(std::move(node->right), successor->value);
        }
        return node;
    }
};
