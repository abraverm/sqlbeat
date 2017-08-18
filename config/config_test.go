// +build !integration

package config

import (
  "fmt"
  "testing"

  "github.com/stretchr/testify/assert"
)

func TestReadConfig(t *testing.T) {
  // Tests with different params from config file
  absPath, err := filepath.Abs("../tests/")

  assert.NotNil(t, absPath)
  assert.Nil(t, err)

  config := &Config{}

  // Reads second config file
  err = cfgfile.Read(config, absPath+"/config2.yml")
  assert.Nil(t, err)

  assert.Equal(t, uint64(0), config.SpoolSize)
}