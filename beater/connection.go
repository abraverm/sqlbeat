package beater

import (
  // "database/sql"
  "fmt"  
)

type Connection struct {
  name      string
  dbType    string
  hostname  string
  port      int
  username  string
  password  string
  connString string
}

// func NewConnection(name string, dbType string, hostname string, port int, username string, password string) error {

//   getConnection()
//   c := &Connection {
//     name: name
//     connString: 
//   }

// }

func (c *Connection) getConnection(dbType string, hostname string, username string, password string, port string, database string, postgresSSLMode string) string {

  connString := ""

  switch dbType {
  case dbtMSSQL:
    connString = fmt.Sprintf("server=%v;user id=%v;password=%v;port=%v;database=%v",
      hostname, username, password, port, database)

  case dbtMySQL:
    connString = fmt.Sprintf("%v:%v@tcp(%v:%v)/%v",
      username, password, hostname, port, database)

  case dbtPSQL:
    connString = fmt.Sprintf("%v://%v:%v@%v:%v/%v?sslmode=%v",
      dbtPSQL, username, password, hostname, port, database, postgresSSLMode)

  }


  // db, err := sql.Open(dbType, connString)
  // if err != nil {
  //   return err
  // }
  // defer db.Close()

  return connString
}