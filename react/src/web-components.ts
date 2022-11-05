import reactToWebComponent from "react-to-webcomponent";
import React from "react";
import ReactDOM from "react-dom/client";
import * as reactComponents from "./index";

/**
 * Export all components as Web Components
 */
Object.keys(reactComponents).forEach((componentName: string) => {
  const component = reactComponents[componentName];
  const WebComponent = reactToWebComponent(
    component,
    React as any,
    ReactDOM as any
  );
  const name = `circuitsvis-${componentName
    .replace(/[^a-zA-Z]+/g, "")
    .toLowerCase()}`;
  window.customElements.define(name, WebComponent as any);
});
