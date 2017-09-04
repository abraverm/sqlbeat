// Query implements a single SQL statement, including the DB connection, 
// frequency of execution and the SQL statement itself.

package beater

import (
  "time"
)

type Query struct {
  query       string             //
  query_type  string
  frequency   time.Duration      
}
