#pragma once

#include <memory>
#include <iostream>
#include <string>



template <class T> class List;

/**
 * @class Node
 * @brief Ein Knoten um Daten zu speichern
 * kann auf einen weiteren Knoten verweisen
 */

template <class T>
class Node{

friend List<T>;

template <class A> using Nodeptr = std::shared_ptr<Node<A>>;

public:

  /** @brief erstellt einen Knoten mit data*/
  Node(std::string name, T data_s);
  Node(std::string name);

  /** @brief gibt den Nachfolger des aktuellen Knotens zurück*/
  Nodeptr<T> getnext()const;

  /** @brief gibt data_ zurück */
  virtual T get_Data();
  /** @brief gibt data_ den neuen Wert data */
  virtual void setData(T data);

  std::string get_name() const;

  void set_name(std::string name);  

private:
  T data_;
  std::string namee;
  Nodeptr<T> next_;
};


template <class T> using Nodeptr = std::shared_ptr<Node<T>>;



#include "node.ipp"