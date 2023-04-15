package botley

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
	"text/template"
)

type ProjectConfig struct {
	ApiTitle       string
	ApiDescription string
	ApiVersion     string
	ContactName    string
	ContactEmail   string
}

func CreateAsset(assetName, dirName string) error {
	newAssetPath := filepath.Join(dirName, assetName+".yml")
	_, err := os.Create(newAssetPath)
	if err != nil {
		return err
	}
	fmt.Printf("%s successfully created\n", assetName)
	return nil
}

func RemoveAsset(assetName, dirName string) error {
	assetPath := filepath.Join(dirName, assetName+".yml")
	err := os.Remove(assetPath)
	if err != nil {
		return err
	}
	return nil
}

func InitProject(projectName string, config ProjectConfig) error {
	dirs := []string{
		filepath.Join(projectName, "schemas"),
		filepath.Join(projectName, "resources"),
		filepath.Join(projectName, "parameters", "query"),
		filepath.Join(projectName, "parameters", "path"),
		filepath.Join(projectName, "responses"),
	}

	for _, dir := range dirs {
		err := os.MkdirAll(dir, os.ModePerm)
		if err != nil {
			return err
		}
	}

	configPath := filepath.Join(projectName, "project_config.yml")
	configData := fmt.Sprintf("api_title: %s\napi_description: %s\napi_version: %s\ncontact_name: %s\ncontact_email: %s\n",
		config.ApiTitle, config.ApiDescription, config.ApiVersion, config.ContactName, config.ContactEmail)
	err := ioutil.WriteFile(configPath, []byte(configData), 0644)
	if err != nil {
		return err
	}

	return nil
}

func BuildFromTemplate(inputFile, templateFile, dirName, fileName string) error {
	data, err := ioutil.ReadFile(inputFile)
	if err != nil {
		return err
	}

	tmpl, err := template.ParseFiles(templateFile)
	if err != nil {
		return err
	}

	outputFile := filepath.Join(dirName, fileName)
	f, err := os.Create(outputFile)
	if err != nil {
		return err
	}
	defer f.Close()

	err = tmpl.Execute(f, string(data))
	if err != nil {
		return err
	}

	return nil
}

func InsertIntoIndex(assetName, dirName string) error {
	indexFile := filepath.Join(dirName, "_index.yml")
	data, err := ioutil.ReadFile(indexFile)
	if err != nil {
		return err
	}

	lines := strings.Split(string(data), "\n")
	newLine := fmt.Sprintf("%s:\n  $ref: '%s.yml'", assetName, assetName)
	lines = append(lines, newLine)

	err = ioutil.WriteFile(indexFile, []byte(strings.Join(lines, "\n")), 0644)
	if err != nil {
		return err
	}

	fmt.Printf("%s inserted to %s/_index.yml\n", assetName, dirName)
	return nil
}

func RemoveFromIndex(assetName, dirName string) error {
	indexFile := filepath.Join(dirName, "_index.yml")
	data, err := ioutil.ReadFile(indexFile)
	if err != nil {
		return err
	}

	lines := strings.Split(string(data), "\n")
	for i, line := range lines {
		if strings.HasPrefix(line, assetName+":") {
			lines = append(lines[:i], lines[i+2:]...)
			break
		}
	}

	err = ioutil.WriteFile(indexFile, []byte(strings.Join(lines, "\n")), 0644)
	if err != nil {
		return err
	}

	return nil
}

func ResourceBuilder(resource string) error {
	fileName := resource + ".yml"
	return BuildFromTemplate(resource, "templates/path.mustache", "resources", fileName)
}

func ResponseBuilder(response string) error {
	fileName := response + ".yml"
	return BuildFromTemplate(response, "templates/response.mustache", "responses", fileName)
}

func ParameterBuilder(parameter string) error {
	fileName := parameter + ".yml"
	return BuildFromTemplate(parameter, "templates/parameter.mustache", "parameters", fileName)
}

func SchemaBuilder(schema string) error {
	fileName := schema + ".yml"
	return BuildFromTemplate(schema, "templates/schema.mustache", "schemas", fileName)
}

func InsertResourcePaths(resource string) error {
	return InsertIntoIndex(resource, "resources")
}

func InsertParameter(paramType, param string) error {
	return InsertIntoIndex(paramType+"."+param, "parameters")
}

func InsertResponse(statusCode, response string) error {
	return InsertIntoIndex(statusCode+"."+response, "responses")
}

func InsertSchema(schema string) error {
	return InsertIntoIndex(schema, "schemas")
}

func SayHi(){
	fmt.Println("Hello! I'm Botley, your friendly virtual assistant. My job is to help you with API development by providing a set of utilities to manage OpenAPI specifications.")
	fmt.Println("My functions include creating and removing files and directories, building new assets from templates, and inserting and removing data from index files. I also provide a user-friendly prompt to help you set up a new project with ease.")
	fmt.Println("With my help, you can easily manage multiple OpenAPI specifications tailored to specific tooling and ensure that your APIs are consistent and maintainable. I'm here to help you save time and simplify your API development process.")
}