#pragma once

#include <memory>
#include "node.hpp"
#include <iostream>




template <class T>
class List {
public:
  List();

  // Insert and delete Nodes
  /** Pushes a new Node at the beginning of the List with value x */
  Nodeptr<T> push(std::string name, T x);
  /** Pushes a new Node at the beginning of the List with value x */
  Nodeptr<T> push(std::string name);

  /** Pushes a new Node between current and the Node after current with value T */
  Nodeptr<T> push_after(const Nodeptr<T>& current, std::string name,  T x);
  /** Pushes a new Node between current and the Node after current with value T */
  Nodeptr<T> push_after(const Nodeptr<T>& current, std::string name);

  /** Deletes the first Node in the List */
  Nodeptr<T> pop();

  /** Deletes the Node between current and the Node after current */
  Nodeptr<T> pop_after(const Nodeptr<T>& current);

  /** Get the next Node of the current List */
  Nodeptr<T> next(const Nodeptr<T>&) const;

  /** Print the current List */
  void print() const;

  /** returns the number of elements in the Liste */
  int size()const;

  /** returns true if the input is the last node of the List and false otherwise */
  bool is_last(const Nodeptr<T>& current);

  /** returns the first Element of the List */
  Nodeptr<T> first() const;

  /**  deletes the first element in the List with value */
  Nodeptr<T> erase(const std::string& value);

  bool is_in(std::string name) const;

  
  /** Iterator class for the List like in the Lecture Notes of Alpro */
  class iterator : public std::iterator<std::forward_iterator_tag,Node<T>,std::ptrdiff_t,Nodeptr<T>,Node<T>&>{
    private:
    Nodeptr<T> _p; // Our Iterators in the List should be shared pointer [or at least feel like them]
    public:
    iterator(Nodeptr<T> p) : _p(p) {}

    /** if _p != the Nullpointer ++ should set the Iterator to the next pointer */
    iterator& operator++() { if(_p) { _p = _p->next_; } return *this;}

    /** if _p != the Nullpointer ++ should set the Iterator to the next pointer */
    iterator operator++(int) {iterator retval = *this; ++(*this); return retval;}

    /** Iterator's should be equal if their Pointers work on the same Object [dasselbe nicht das gleiche!] */
    bool operator==(iterator other) const {return _p == other._p;} 
    
    /** Iterator's should be equal if their Pointers work on the same Object [dasselbe nicht das gleiche!] */
    bool operator!=(iterator other) const {return !(*this == other);}
    
    /** returns the object the pointer works on */
    Node<T>& operator*() const {return *_p;} 
  };

  /**  begin()-Function returns Iterator to the beginning */
  iterator begin() {return this->head;};

  /**  end()-Function returns Iterator of the nullptr so you can see the End of the List */
  iterator end() {return Nodeptr<T>(nullptr);};

private:
  Nodeptr<T> head;
  int size_;

  /** helps if you inherite from a class that already has a push function */
  Node<T>* push_c(std::string name, T Elt);
  /** helps if you inherite from a class that already has a push function */
  Node<T>* push_c(std::string name);
  /** helps if you inherite from a class that already has a pop function */
  Node<T>* pop_c();
};


#include "list.ipp"