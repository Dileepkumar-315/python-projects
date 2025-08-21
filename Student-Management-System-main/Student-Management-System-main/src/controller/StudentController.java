package controller;


import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import application.DBConnection;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import model.Student;


public class StudentController {

    @FXML
    private TextField nameField;

    @FXML
    private TextField rollField;
    
    @FXML
    private TextField searchField;
    

    @FXML
    private TextField courseField;

    @FXML
    private TextField semesterField;

    @FXML
    private TextField emailField;

    @FXML
    private TextField phoneField;
    
    @FXML private TableView<Student> studentTable;
    private ObservableList<Student> studentList = FXCollections.observableArrayList();

    
    @FXML private TableColumn<Student, String> nameCol;
    @FXML private TableColumn<Student, String> rollCol;
    @FXML private TableColumn<Student, String> courseCol;
    @FXML private TableColumn<Student, String> semesterCol;
    @FXML private TableColumn<Student, String> emailCol;
    @FXML private TableColumn<Student, String> phoneCol;
    
    @FXML
    public void initialize() {
        // Bind column values once during initialization
        nameCol.setCellValueFactory(new PropertyValueFactory<>("name"));
        rollCol.setCellValueFactory(new PropertyValueFactory<>("rollNumber"));
        courseCol.setCellValueFactory(new PropertyValueFactory<>("course"));
        semesterCol.setCellValueFactory(new PropertyValueFactory<>("semester"));
        emailCol.setCellValueFactory(new PropertyValueFactory<>("email"));
        phoneCol.setCellValueFactory(new PropertyValueFactory<>("phone"));

         // Load all students into studentList
    }
    
    


    @FXML
    private void insertStudent() {
        String name = nameField.getText();
        String roll = rollField.getText();
        String course = courseField.getText();
        String semester = semesterField.getText();
        String email = emailField.getText();
        String phone = phoneField.getText();

        if (name.isEmpty() || roll.isEmpty()) {
            showAlert(Alert.AlertType.ERROR, "Name and Roll Number are required.");
            return;
        }

        String sql = "INSERT INTO students (name, roll_number, course, semester, email, phone) VALUES (?, ?, ?, ?, ?, ?)";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, name);
            stmt.setString(2, roll);
            stmt.setString(3, course);
            stmt.setString(4, semester);
            stmt.setString(5, email);
            stmt.setString(6, phone);

            int rowsInserted = stmt.executeUpdate();

            if (rowsInserted > 0) {
                showAlert(Alert.AlertType.INFORMATION, "Student inserted successfully!");
                clearFields();
            } else {
                showAlert(Alert.AlertType.ERROR, "Insertion failed.");
            }

        } catch (Exception e) {
            e.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Database error: " + e.getMessage());
        }
    }

    
    
    @FXML
    private void updateStudent() {
        String roll = rollField.getText();

        if (roll.isEmpty()) {
            showAlert(Alert.AlertType.WARNING, "Please enter Roll Number to update.");
            return;
        }

        String sql = "UPDATE students SET name = ?, course = ?, semester = ?, email = ?, phone = ? WHERE roll_number = ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, nameField.getText());
            stmt.setString(2, courseField.getText());
            stmt.setString(3, semesterField.getText());
            stmt.setString(4, emailField.getText());
            stmt.setString(5, phoneField.getText());
            stmt.setString(6, roll);

            int rowsUpdated = stmt.executeUpdate();

            if (rowsUpdated > 0) {
                showAlert(Alert.AlertType.INFORMATION, "Student updated successfully!");
                clearFields();
            } else {
                showAlert(Alert.AlertType.WARNING, "No student found with Roll Number: " + roll);
            }

        } catch (Exception e) {
            e.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Database error: " + e.getMessage());
        }
    }
    
    @FXML
    private void deleteStudent() {
        String roll = rollField.getText();

        if (roll.isEmpty()) {
            showAlert(Alert.AlertType.WARNING, "Please enter Roll Number to delete.");
            return;
        }

        String sql = "DELETE FROM students WHERE roll_number = ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, roll);
            int rowsDeleted = stmt.executeUpdate();

            if (rowsDeleted > 0) {
                showAlert(Alert.AlertType.INFORMATION, "Student deleted successfully!");
                clearFields();
            } else {
                showAlert(Alert.AlertType.WARNING, "No student found with Roll Number: " + roll);
            }

        } catch (Exception e) {
            e.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Database error: " + e.getMessage());
        }
    }
    
    
    @FXML
    private void loadStudents() {
        studentList.clear(); // Clear previous

        String sql = "SELECT * FROM students";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                studentList.add(new Student(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("roll_number"),
                        rs.getString("course"),
                        rs.getString("semester"),
                        rs.getString("email"),
                        rs.getString("phone")
                ));
            }

            // Bind column values only once
            //idCol.setCellValueFactory(new PropertyValueFactory<>("id"));
            nameCol.setCellValueFactory(new PropertyValueFactory<>("name"));
            rollCol.setCellValueFactory(new PropertyValueFactory<>("rollNumber"));
            courseCol.setCellValueFactory(new PropertyValueFactory<>("course"));
            semesterCol.setCellValueFactory(new PropertyValueFactory<>("semester"));
            emailCol.setCellValueFactory(new PropertyValueFactory<>("email"));
            phoneCol.setCellValueFactory(new PropertyValueFactory<>("phone"));

            studentTable.setItems(studentList); // Show all students initially

        } catch (Exception e) {
            e.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Error loading students: " + e.getMessage());
        }
    }
    
    @FXML
    private void handleSearch(ActionEvent event) {
        String keyword = searchField.getText().trim();

        if (keyword.isEmpty()) {
            studentTable.setItems(FXCollections.observableArrayList()); // Clear table
            return;
        }

        ObservableList<Student> filteredList = FXCollections.observableArrayList();

        String sql = "SELECT * FROM students WHERE LOWER(name) LIKE ? OR LOWER(roll_number) LIKE ?";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            String searchPattern = "%" + keyword.toLowerCase() + "%";
            stmt.setString(1, searchPattern);
            stmt.setString(2, searchPattern);

            ResultSet rs = stmt.executeQuery();

            while (rs.next()) {
                filteredList.add(new Student(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("roll_number"),
                        rs.getString("course"),
                        rs.getString("semester"),
                        rs.getString("email"),
                        rs.getString("phone")
                ));
            }

            studentTable.setItems(filteredList);

        } catch (Exception e) {
            e.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Search error: " + e.getMessage());
        }
    }
    
    @FXML
    private void handleClearTable() {
        studentTable.getItems().clear();
    }
    
 









    private void showAlert(Alert.AlertType type, String message) {
        Alert alert = new Alert(type);
        alert.setTitle("Message");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    private void clearFields() {
        nameField.clear();
        rollField.clear();
        courseField.clear();
        semesterField.clear();
        emailField.clear();
        phoneField.clear();
    }

    private void clearFieldsExceptRoll() {
        nameField.clear();
        courseField.clear();
        semesterField.clear();
        emailField.clear();
        phoneField.clear();
    }
}
