module StudentManagementProject {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;
	requires javafx.base;

    opens controller to javafx.fxml;
    opens views to javafx.fxml;  // if you're using fxml inside views
    opens application to javafx.graphics;
    opens model to javafx.base;

    exports controller;
}
